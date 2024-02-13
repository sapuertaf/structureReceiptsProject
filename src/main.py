from services.event_logger import EventLogger
from adapters.cloud_event_model_adapter import CloudEventModelAdapter
from services.cloud_config import CloudConfig
from services.model import Model
from adapters.model_response_receipt_data_adapter import ModelResponseReceiptDataAdapter
from receipt_data import ReceiptData
from stages.load import LoadStage
from exceptions.custom_exceptions import ProcessError

from cloudevents.http import CloudEvent
from vertexai.preview.generative_models import Part
from pandas import DataFrame


def structure_receipt_img_(cloud_event: CloudEvent):
    event_logger = EventLogger().build()
    try:
        ce_model_adapter = CloudEventModelAdapter(cloud_event, event_logger)
        config = CloudConfig()
        model = Model(config, event_logger)

        img: Part = ce_model_adapter.get_cloud_storage_img()
        response: str = model.build().ask_prompt(img)
        print(response)  # TODO: Delete this print

        mock_response = """
        {
            "persona" : "Juan Perez",
            "direccion": "Calle n #x-y"
        }
        """  # TODO: Delete this mock use
        response = mock_response  # TODO: Delete this mock use

        model_receipt_adapter = ModelResponseReceiptDataAdapter(response)
        receipt_data: DataFrame = ReceiptData(model_receipt_adapter.jsonify_response()).structure_data()

        LoadStage(config, event_logger).build(receipt_data).execute()
    except Exception as e:
        event_logger.error(
            ProcessError("", e)
        )


if __name__ == "__main__":
    event = CloudEvent({
        "source": None,
        "type": "HTTP"
    }, {
        "bucket": "gemini-images-871145895348",
        "name": "receipt_1.jpeg"
    })
    structure_receipt_img_(event)
