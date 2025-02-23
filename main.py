from dotenv import load_dotenv, find_dotenv
import openai
import time
import logging

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

assist_id = "asst_jHcLN1p3tlb4PFzx1CYNHyNG"
thread_id =  "thread_qq9YERDOM338mOVmOBBczFlt"

message = client.beta.threads.messages.create(
    thread_id = thread_id,
    content = "What is the best workout for building muscle?",
    role = "user"
)

run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assist_id,
    instructions="Please adress a user as James Bond"
)

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """

    Waits for a run to complete and prints the elapsed time.:param client: The OpenAI client object.
    :param thread_id: The ID of the thread.
    :param run_id: The ID of the run.
    :param sleep_interval: Time in seconds to wait between checks.
    """
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")
                # Get messages here once Run is completed!
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)


# === Run ===
wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

# ==== Steps --- Logs ==
run_steps = client.beta.threads.runs.steps.list(thread_id=thread_id, run_id=run.id)
print(f"Steps---> {run_steps.data[0]}")