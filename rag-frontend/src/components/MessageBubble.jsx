export default function MessageBubble({ role, text, confidence }) {
  return (
    <div className={`bubble ${role}`}>
      <p>{text}</p>
      {confidence && (
        <span className="confidence-score">
          Confidence: {confidence}%
        </span>
      )}
    </div>
  );
}
