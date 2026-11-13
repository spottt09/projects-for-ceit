from transformers import pipeline

print("starting Qwen3...", flush=True)

pipe = pipeline("text-generation", model="Qwen/Qwen3-0.6B", device="cpu")

while True:
	question = input("\nYOU: ")

	if question.lower() == "exit":
		break

	message = [{"role":"user", "content":question}]

	print("Generating response...", flush=True)

	result = pipe(message, max_new_tokens=128, return_full_text=False)

	print("Qwen: ", result[0]["generated_text"])
