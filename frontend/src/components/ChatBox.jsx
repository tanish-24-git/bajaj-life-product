import React, { useEffect, useRef } from 'react'

function ChatBox({ messages, loading }) {
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const renderMessage = (msg, index) => {
    const isBot = msg.sender === 'bot'
    
    // Check if message contains a buy link
    // We do a simple heuristic check for demonstration
    const hasBuyLink = msg.text.includes("http") && (msg.text.includes("buy") || msg.text.includes("checkout"))
    
    return (
      <div key={index} className={`message ${isBot ? 'bot' : 'user'}`}>
        <div className="text-content">
            {msg.text.split('\n').map((line, i) => <p key={i}>{line}</p>)}
        </div>
        
        {isBot && hasBuyLink && (
            <div className="buy-action">
                <a href="https://www.bajajlifeinsurance.com/" target="_blank" rel="noreferrer" className="buy-btn">
                    Proceed to Buy on Bajaj Life
                </a>
            </div>
        )}
      </div>
    )
  }

  return (
    <div className="chat-box">
      {messages.map(renderMessage)}
      {loading && <div className="message bot typing">Thinking...</div>}
      <div ref={bottomRef} />
    </div>
  )
}

export default ChatBox
