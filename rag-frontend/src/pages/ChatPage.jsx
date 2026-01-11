// import ChatWindow from "../components/ChatWindow";
// import PdfUploader from "../components/PdfUploader";
// import "../styles/chat.css";

// export default function ChatPage() {
//   return (
//     <div>
//       <h1>DocuMind AI</h1>
//       <p>Your intelligent documentation assistant</p>

      
//       {/* 🔥 PDF Upload */}
//       <PdfUploader />

//       {/* 💬 Chat */}
//       <ChatWindow />
//     </div>

    
//   );
// }
import ChatWindow from "../components/ChatWindow";
import PdfUploader from "../components/PdfUploader";
import "../styles/chat.css";

export default function ChatPage() {
  return (
    <div className="chat-page">
      <h1 className="app-title">DocuMind AI</h1>
      <p className="app-subtitle">
        Your intelligent documentation assistant
      </p>

      {/* 📄 PDF Upload */}
      <PdfUploader />

      {/* 💬 Chat */}
      <ChatWindow />
    </div>
  );
}
