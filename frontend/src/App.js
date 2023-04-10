// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


// import React from 'react';
// import './App.css';
// import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
// import { MainContainer, ChatContainer, MessageList, MessageInput } from '@chatscope/chat-ui-kit-react';

// function App() {
//   return (
//     <div className="App">
//       <MainContainer>
//         <ChatContainer>
//           <MessageList />
//           <MessageInput placeholder="Type a message" />
//         </ChatContainer>
//       </MainContainer>
//     </div>
//   );
// }

// export default App;


import React, { useState } from "react";
import "./App.css";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import {
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
} from "@chatscope/chat-ui-kit-react";

function App() {
  const [messages, setMessages] = useState([
    {
      message: "Hello! How can I help you?",
      sentTime: "just now",
      direction: "incoming",
    },
  ]);

  const sendMessage = async (messageText) => {
    // Add user's message to the list
    setMessages((prevMessages) => [
      ...prevMessages,
      {
        message: messageText,
        sentTime: "just now",
        direction: "outgoing",
      },
    ]);

    // Send message to the API and get a response
    const response = await fetch("http://localhost:8001/chatbot_endpoint", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: messageText }),
    });

    const data = await response.json();

    // Add the bot's response to the list
    setMessages((prevMessages) => [
      ...prevMessages,
      {
        message: data.reply,
        sentTime: "just now",
        direction: "incoming",
      },
    ]);
  };

  return (
    <div className="App">
      <ChatContainer>
        <MessageList>
          {messages.map((msg, index) => (
            <Message key={index} model={msg} />
          ))}
        </MessageList>
        <MessageInput
          placeholder="Type your message here..."
          onSend={(messageText) => sendMessage(messageText)}
        />
      </ChatContainer>
    </div>
  );
}

export default App;

