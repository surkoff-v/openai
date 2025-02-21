from dotenv import load_dotenv, find_dotenv
import openai;

load_dotenv()

client = openai.Client()

model = "gpt-3.5-turbo-16k"

# personal_trainer_asist = client.beta.assistants.create(
#     name="Personal Trainer Assistant",
#     instructions="You are a personal trainer",
#     model=model,
# )

# print(personal_trainer_asist.id)




# thread = client.beta.threads.create(
#     messages=[
#          {"role": "user", "content": "What is the best workout for building muscle?"}
#     ]
 
          
# )

# print(thread.id)

assist_id = asst_jHcLN1p3tlb4PFzx1CYNHyNG
thread_id =  thread_qq9YERDOM338mOVmOBBczFlt

client.beta.threads.messages.create(
    thread_id=thread_id,
    messages=[
        {"role": "user", "content": "What is the best workout for building muscle?"}
    ]
)