import time
import azure.functions as func
import logging

# from lib.config import Config
# from lib.cosmo import CosmoDb
from lib.message import CompletionMessage

logging.basicConfig(level=logging.INFO)

logging.info("starting...")

app = func.FunctionApp()
# config = Config()
# cosmo = CosmoDb()

logging.info("init complete")

def process_message(message: CompletionMessage):
    """proccesses a completion request from the queue and writes the response to cosmosdb"""

    start_time = time.time()
    response_text, success, input_tokens, output_tokens = "", False, 0, 0
    ai_exec_time = time.time() - start_time

    sql_exec_time = 0
    cols = 0

    # cosmo.write(
    #     completion_id=message.completion_id,
    #     user_id=message.user_id,
    #     diocese_id=message.diocese_id,
    #     church_id=message.church_id,
    #     user_prompt=message.user_prompt,
    #     error="",
    #     success=success,
    #     input_tokens=input_tokens,
    #     output_tokens=output_tokens,
    #     ai_exec_time=ai_exec_time,
    #     sql_exec_time=sql_exec_time,
    #     cols=cols,
    #     sql_raw="",
    #     sql_with_permissions="",
    #     tables=["table"],
    # )


@app.function_name(name="completions")
@app.queue_trigger(
    arg_name="msg", queue_name="completions", connection="AzureWebJobsStorage"
)
def main(msg: func.QueueMessage) -> None:
    try:
        body = msg.get_json()
        logging.info(f"processing {str(body)}")

        message = CompletionMessage(
            user_id=body.get("user_id"),
            diocese_id=body.get("diocese_id"),
            church_id=body.get("church_id"),
            completion_id=body.get("completion_id"),
            user_prompt=body.get("user_prompt"),
        )

        process_message(message)

        logging.info(f"complete {message.completion_id}")

    except Exception as e:
        logging.exception(e)
        raise
