import { useState, useEffect, useRef } from 'react';
import './TitinVisualizer.css';

const TitinVisualizer = () => {
  const [words, setWords] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(-1);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [isCached, setIsCached] = useState(false);
  const currentWordRef = useRef(null);
  const audioCache = useRef({});
  const playWordRef = useRef(null);

  // Register Service Worker for caching audio files
  useEffect(() => {
    if ('serviceWorker' in navigator) {
      // Check if service worker is already registered
      navigator.serviceWorker.getRegistration('/').then((existingRegistration) => {
        if (existingRegistration) {
          // Check if already cached
          if (navigator.serviceWorker.controller) {
            setIsCached(true);
          }
          return;
        }
        
        // Register new service worker
        navigator.serviceWorker.register('/sw.js')
          .then((registration) => {
            // Check if already cached
            if (navigator.serviceWorker.controller) {
              setIsCached(true);
            }
            // Listen for SW updates
            registration.addEventListener('updatefound', () => {
              const newWorker = registration.installing;
              newWorker.addEventListener('statechange', () => {
                if (newWorker.state === 'activated') {
                  setIsCached(true);
                }
              });
            });
          })
          .catch(() => {
            // Silent fail in production
          });
      });
      
      // Listen for messages from SW
      navigator.serviceWorker.addEventListener('message', (event) => {
        if (event.data && event.data.type === 'CACHE_CLEARED') {
          setIsCached(false);
        }
      });
    }
  }, []);

  // Load titin words on mount
  useEffect(() => {
    fetch('/titin_chemical_name.txt')
      .then(response => response.text())
      .then(text => {
        const wordList = text.trim().split(/\s+/).filter(word => word.length > 0);
        setWords(wordList);
        setIsLoading(false);
      })
      .catch(() => {
        setIsLoading(false);
      });
  }, []);

  // Auto-scroll to current word
  useEffect(() => {
    if (currentWordRef.current) {
      currentWordRef.current.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
      });
    }
  }, [currentIndex]);

  // Play audio for word at index
  const playWord = (index) => {
    if (index < 0 || index >= words.length) {
      setIsPlaying(false);
      return;
    }

    // Highlight the word BEFORE playing audio
    setCurrentIndex(index);

    const word = words[index].toLowerCase();
    
    // Use cached audio or create new
    if (!audioCache.current[word]) {
      audioCache.current[word] = new Audio(`/audio_words/${word}.mp3`);
    }
    
    const currentAudio = audioCache.current[word];
    currentAudio.currentTime = 0;
    
    // Preload next audio
    if (index + 1 < words.length) {
      const nextWord = words[index + 1].toLowerCase();
      if (!audioCache.current[nextWord]) {
        audioCache.current[nextWord] = new Audio(`/audio_words/${nextWord}.mp3`);
        audioCache.current[nextWord].load();
      }
    }
    
    // Set up ended event BEFORE playing - use index directly to avoid stale closure
    currentAudio.onended = () => {
      const nextIndex = index + 1;
      if (nextIndex < words.length) {
        playWord(nextIndex);
      } else {
        setIsPlaying(false);
        setCurrentIndex(-1);
      }
    };
    
    currentAudio.play()
      .catch(() => {
        playWord(index + 1);
      });
  };

  // Store playWord in ref for access in useEffect
  playWordRef.current = playWord;

  // Playback controls
  const handlePlay = () => {
    setIsPlaying(true);
    const startIndex = currentIndex >= 0 ? currentIndex : 0;
    playWord(startIndex);
  };

  const handlePause = () => {
    setIsPlaying(false);
    // Pause all cached audios
    Object.values(audioCache.current).forEach(audio => {
      if (audio && !audio.paused) {
        audio.pause();
      }
    });
  };

  const handleStop = () => {
    setIsPlaying(false);
    setCurrentIndex(-1);
    // Stop all cached audios
    Object.values(audioCache.current).forEach(audio => {
      if (audio) {
        audio.pause();
        audio.currentTime = 0;
      }
    });
  };

  const handleSkipNext = () => {
    if (currentIndex < words.length - 1) {
      playWord(currentIndex + 1);
    }
  };

  const handleSkipPrev = () => {
    if (currentIndex > 0) {
      playWord(currentIndex - 1);
    }
  };

  if (isLoading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading the longest word in the world...</p>
      </div>
    );
  }

  return (
    <div className="titin-visualizer">
      <div className="header">
        <h1>Titin Protein Visualizer</h1>
        <p className="subtitle">
          The chemical name of titin - {words.length.toLocaleString()} amino acids
          {isCached && <span className="cache-indicator" title="Audio files cached for offline use"> ● Cached</span>}
        </p>
      </div>

      <div className="controls">
        <button 
          onClick={handleSkipPrev} 
          disabled={currentIndex <= 0 || !isPlaying}
          className="control-btn"
        >
          ⏮ Previous
        </button>
        
        {!isPlaying ? (
          <button onClick={handlePlay} className="control-btn play-btn">
            ▶ Play
          </button>
        ) : (
          <button onClick={handlePause} className="control-btn pause-btn">
            ⏸ Pause
          </button>
        )}
        
        <button onClick={handleStop} className="control-btn">
          ⏹ Stop
        </button>
        
        <button 
          onClick={handleSkipNext} 
          disabled={currentIndex >= words.length - 1 || !isPlaying}
          className="control-btn"
        >
          Next ⏭
        </button>

        {currentIndex >= 0 && (
          <span className="progress-indicator">
            {currentIndex + 1} / {words.length}
          </span>
        )}
      </div>

      <div className="words-container">
        {words.map((word, index) => (
          <span
            key={index}
            ref={index === currentIndex ? currentWordRef : null}
            className={`word ${index === currentIndex ? 'active' : ''} ${index < currentIndex ? 'played' : ''}`}
            onClick={() => {
              if (!isPlaying) {
                setIsPlaying(true);
                playWord(index);
              }
            }}
          >
            {word}
          </span>
        ))}
      </div>
    </div>
  );
};

export default TitinVisualizer;
