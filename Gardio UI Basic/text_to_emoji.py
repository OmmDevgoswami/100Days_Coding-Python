import gradio as gr

def text_to_emoji(text):
    emoji_map = {
        "happy": "😊", "sad": "😢", "love": "❤️", "angry": "😠",
        "excited": "🤩", "bored": "😐", "tired": "😴", "food": "🍕",
        "fire": "🔥", "laugh": "😂", "dog": "🐶", "cat": "🐱"
    }
    
    words = text.split()
    new_words = []

    for word in words:
        key = word.lower()
        new_words.append(word + " " + emoji_map[key] if key in emoji_map else word)

    return " ".join(new_words)

iface = gr.Interface(
    fn=text_to_emoji,
    inputs="text",
    outputs="text",
    title="📝 Text to Emoji Converter",
    description="Enter a sentence and get instant emojis!",
)

# ✅ Flask-style entry point
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860, share=True)
