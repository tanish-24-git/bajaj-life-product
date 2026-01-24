import { useState, useEffect, useRef } from 'react'
import ChatBox from './components/ChatBox'
import './App.css'

function App() {
  const [messages, setMessages] = useState([
    { 
      sender: 'bot', 
      text: "Hello! I am your Bajaj Life Assistant. I can help you with Term Insurance and Investment plans. How can I assist you today?" 
    }
  ])
  const [input, setInput] = useState('')
  const [voiceEnabled, setVoiceEnabled] = useState(false)
  const [loading, setLoading] = useState(false)
  const audioRef = useRef(null)

  const sendMessage = async () => {
    if (!input.trim()) return

    const userMsg = { sender: 'user', text: input }
    setMessages(prev => [...prev, userMsg])
    setInput('')
    setLoading(true)

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: userMsg.text, enable_voice: voiceEnabled })
      })
      
      const data = await response.json()
      
      // Add Bot Message
      setMessages(prev => [...prev, { 
        sender: 'bot', 
        text: data.response,
        products: data.products_found
      }])

      // Play Audio if enabled and present
      if (data.audio_base64 && voiceEnabled) {
        const audioSrc = `data:audio/mp3;base64,${data.audio_base64}`
        if (audioRef.current) {
          audioRef.current.src = audioSrc
          audioRef.current.play()
        }
      }

    } catch (error) {
      console.error("Error:", error)
      setMessages(prev => [...prev, { sender: 'bot', text: "Sorry, I am having trouble connecting to the server." }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <header className="header">
        <img src="https://www.bajajlifeinsurance.com/content/dam/bagic/logos/bajaj-logo.png" alt="Bajaj Logo" className="logo" />
        <h1>Bajaj Life Sales Assistant</h1>
      </header>
      
      <div className="main-content">
        <div className="controls">
          <label>
            <input 
              type="checkbox" 
              checked={voiceEnabled} 
              onChange={(e) => setVoiceEnabled(e.target.checked)} 
            />
            Enable Voice (PersonaPlex/TTS)
          </label>
        </div>

        <ChatBox messages={messages} loading={loading} />

        <div className="input-area">
          <input 
            type="text" 
            value={input} 
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask about Term Plans, eTouch, Tax Benefits..."
            disabled={loading}
          />
          <button onClick={sendMessage} disabled={loading}>
            {loading ? '...' : 'Send'}
          </button>
        </div>
      </div>
      
      <audio ref={audioRef} hidden />
    </div>
  )
}

export default App
