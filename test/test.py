from transformers import pipeline

# Load the pre-trained summarization model
summarizer = pipeline("summarization", model="google/pegasus-xsum")

text = """Artificial intelligence (AI) is intelligence demonstrated by machines, 
as opposed to the natural intelligence displayed by animals and humans. Leading AI 
textbooks define the field as the study of intelligent agents: any system that 
perceives its environment and takes actions that maximize its chance of achieving 
its goals."""

summary = summarizer(text, max_length=100, min_length=30, do_sample=False)

print(summary[0]['summary_text'])
