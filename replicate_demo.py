import replicate



output = replicate.run(
    "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input={
        "image": "",
        "width": 768,
        "height": 768,
        "prompt": "A youtube thumbnail for a lecture , the lecture is of javascript. The image of the instructor should be same",
        "refine": "expert_ensemble_refiner",
        "scheduler": "K_EULER",
        "lora_scale": 0.6,
        "num_outputs": 1,
        "guidance_scale": 7.5,
        "apply_watermark": False,
        "high_noise_frac": 0.8,
        "negative_prompt": "",
        "prompt_strength": 0.8,
        "num_inference_steps": 25
    }
)
print(output)

# ['https://replicate.delivery/pbxt/VJyWBjIYgqqCCBEhpkCqdevTgAJbl4fg62aO4o9A0x85CgNSA/out-0.png']
# ['https://replicate.delivery/pbxt/VJyWBjIYgqqCCBEhpkCqdevTgAJbl4fg62aO4o9A0x85CgNSA/out-0.png']