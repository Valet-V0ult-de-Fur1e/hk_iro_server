import React from "react";
import Chatbot from "react-chatbot-kit";
import "./Bot.css";

import ActionProvider from "./ActionProvider";
import MessageParser from "./MessageParser";
import config from "./config";

function Bot() {
  return (
    <div className="App">
      <header className="App-header">
        <Chatbot
          config={config}
          actionProvider={ActionProvider}
          messageParser={MessageParser}
        />
      </header>
    </div>
  );
}

export default Bot;
