import React, { useState, useRef } from "react";
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

  const fileInputRef = useRef();

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];

    // Create a FormData instance
    const formData = new FormData();

    // Append the file to the form data
    formData.append('pdf_file', file);

    // Send a POST request to the server with the form data
    const response = await fetch("http://localhost:8001/index", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log(data);
  };

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
          attachButton={true}
          onAttachClick={() => {
            console.log('Attachment button clicked');
            console.log('fileInputRef.current:', fileInputRef.current);
            fileInputRef.current.click();
          }}
        />
      </ChatContainer>
      <input
        type="file"
        ref={fileInputRef}
        style={{ display: 'none' }}
        onChange={handleFileUpload}
      />
    </div>
  );

}

export default App;
