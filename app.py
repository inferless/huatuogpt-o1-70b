import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"]='1'
from huggingface_hub import snapshot_download
from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer
import torch

class InferlessPythonModel:
    def initialize(self):
        model_id = "FreedomIntelligence/HuatuoGPT-o1-70B"
        snapshot_download(repo_id=model_id,allow_patterns=["*.safetensors"])
        quantization_config = BitsAndBytesConfig(load_in_4bit=True,
                                                 bnb_4bit_compute_dtype=torch.bfloat16
                                                )
        self.model = AutoModelForCausalLM.from_pretrained(
                                                        model_id, 
                                                        quantization_config=quantization_config,
                                                        device_map="auto"
                                                        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)

    def infer(self, inputs):
        prompt = inputs["prompt"]
        temperature = float(inputs.get("temperature", 1.0))
        top_p = float(inputs.get("top_p", 1.0))
        top_k = int(inputs.get("top_k", 50))
        length_penalty = float(inputs.get("length_penalty", 1.0))
        repetition_penalty = float(inputs.get("repetition_penalty", 1.0))
        early_stopping = inputs.get("early_stopping", False)
        max_new_tokens = int(inputs.get("max_new_tokens", 128))
        min_new_tokens = int(inputs.get("min_new_tokens", 20))
        do_sample = inputs.get("do_sample", False)
        num_beams = int(inputs.get("num_beams", 1))

        messages = [{"role": "user", "content": prompt}]      
        chat_format = self.tokenizer.apply_chat_template(messages, tokenize=False,add_generation_prompt=True)
        inputs = self.tokenizer(chat_format, return_tensors="pt").to(0)
      
        outputs = self.model.generate(**inputs,
                                      temperature=temperature,
                                      top_p=top_p,
                                      top_k=top_k,
                                      length_penalty=length_penalty,
                                      repetition_penalty=repetition_penalty,
                                      early_stopping=early_stopping,
                                      max_new_tokens=max_new_tokens,
                                      min_new_tokens=min_new_tokens,
                                      do_sample=do_sample,
                                      num_beams=num_beams)
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"generated_text":generated_text}


    def finalize(self):
        self.generator = None
