import { useState, useEffect, useRef } from "react";
import { askQuestion } from "../api/ragApi";
import MessageBubble from "./MessageBubble";
import InputBox from "./InputBox";
import SourcePanel from "./SourcePanel";
import "../styles/chat.css";

export default function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const data = await askQuestion(input);

      const botMsg = {
        role: "assistant",
        text: data.answer || "No answer found.",
        confidence: data.confidence, // Pass confidence
      };

      setMessages((prev) => [...prev, botMsg]);
      setSources(data.sources || []);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: "⚠️ Error fetching response." },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="chat-wrapper">
      <div className="chat-window">
        {messages.map((msg, index) => (
          <MessageBubble
            key={index}
            role={msg.role}
            text={msg.text}
            confidence={msg.confidence} // Pass confidence prop
          />
        ))}

        {loading && (
          <MessageBubble
            role="assistant"
            text="Thinking..."
            loading
          />
        )}
        <div ref={messagesEndRef} />
      </div>

      <SourcePanel sources={sources} />

      <InputBox
        value={input}
        onChange={setInput}
        onSend={sendMessage}
        loading={loading}
      />
    </div>
  );
}
