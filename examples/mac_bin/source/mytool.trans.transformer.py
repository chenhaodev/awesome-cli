from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import sys

mode_name = 'Helsinki-NLP/opus-mt-en-zh' 
tokenizer = AutoTokenizer.from_pretrained(mode_name)
model = AutoModelForSeq2SeqLM.from_pretrained(mode_name)
translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)

result = translation(sys.argv[1:], max_length=2000)
print(result)

'''
TEST: 
text = "Skin disease diagnosis and image processing have been greatly influenced by advancements in artificial intelligence (AI) and image analysis techniques. Deep learning models, such as convolutional neural networks (CNNs), have shown promising results in the accurate diagnosis of skin lesions from clinical and dermoscopic images Young et al. [21][22]. These models are often trained on large databases of dermatology images, enabling them to learn patterns and features associated with different skin diseases [19]. Conventional imaging approaches, such as monochrome or RGB color imaging, have limitations in resolving heterogeneous skin lesions and may lead to diagnostic inaccuracies [20]. However, AI-based image processing techniques can overcome these limitations by extracting relevant features and patterns from skin images, enabling more accurate and reliable diagnosis [19]. In addition to diagnosis, AI has also been applied to other aspects of skin disease management. For example, AI-based computer-aided diagnosis (CAD) systems have been developed to assist clinicians in identifying and analyzing skin lesions in a timely and accurate manner [24]. These systems combine medical image analysis and computer image processing techniques to quantify and judge the characteristics of skin lesions [24]. Furthermore, the psychosocial impact of skin diseases on patients has been a topic of interest. Studies have identified various factors that influence psychosocial adaptation in patients with skin diseases, including demographic factors, disease-related factors, psychological factors, and social factors [23]. Adjuvant care programs, such as cognitive behavioral training and educational training, have been found to be beneficial in helping patients cope with the psychosocial impacts of skin diseases [23]. Overall, AI and image processing techniques have significantly advanced the field of dermatology, particularly in the diagnosis and management of skin diseases. These technologies have the potential to improve diagnostic accuracy, enhance patient care, and contribute to a better understanding of skin diseases. However, further research and clinical validation are needed to ensure the reliability and effectiveness of AI-based systems in real-world clinical settings."

result = translation(text, max_length=2000)
print(result)

'''
