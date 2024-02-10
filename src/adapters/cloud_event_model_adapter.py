import mimetypes

from cloudevents.http import CloudEvent
from vertexai.preview.generative_models import Part


class CloudEventModelAdapter:
    """
    Adapter class to handle CloudEvents and interact with a generative model.

    This class provides methods to extract image data from CloudEvents and convert it to Part objects.
    """
    def __init__(self, cloud_event: CloudEvent):
        """
        Initialize the CloudEventModelAdapter with the given CloudEvent.

        Args:
            cloud_event (CloudEvent): The CloudEvent instance containing image data.
        """
        self._cloud_event = cloud_event
        self._event_data = self._cloud_event.data

    @property
    def cloud_event(self) -> CloudEvent:
        """
        Get the current CloudEvent.

        Returns:
            CloudEvent: The current CloudEvent instance.
        """
        return self._cloud_event

    @cloud_event.setter
    def cloud_event(self, new_cloud_event: CloudEvent) -> None:
        """
        Set a new CloudEvent.

        Args:
            new_cloud_event (CloudEvent): The new CloudEvent instance.
        """
        self._cloud_event = new_cloud_event
        self._event_data = new_cloud_event.data

    def _get_img_mime_type(self) -> str:
        """
        Get the MIME type of the image.

        Returns:
            str: The MIME type of the image.
        """
        mime_type, _ = mimetypes.guess_type(self._event_data["name"])
        return mime_type

    def get_cloud_storage_img(self) -> Part:
        """
        Get image data from Cloud Storage as a Part object.

        Returns:
            Part: The image data as a Part object.
        """
        gcs_img_path = f"gs://{self._event_data['bucket']}/{self._event_data['name']}"
        return Part.from_uri(gcs_img_path,
                             mime_type=self._get_img_mime_type())


if __name__ == "__main__":
    cloud_event = CloudEvent({"source": None, "type": "HTTP"}, {
        "bucket": "gemini-images-871145895348",
        "name": "receipt_1.jpeg"
    })
    print(CloudEventModelAdapter(cloud_event).get_cloud_storage_img())
