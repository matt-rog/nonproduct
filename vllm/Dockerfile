FROM vllm/vllm-openai:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

RUN uv pip install --system git+https://github.com/huggingface/transformers.git

CMD ["--model", "Qwen/Qwen3-0.6B"]