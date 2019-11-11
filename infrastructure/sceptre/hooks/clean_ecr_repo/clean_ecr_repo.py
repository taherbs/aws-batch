"""
Delete all images from designated Ecr repository
"""

from sceptre.hooks import Hook
import boto3

class CleanEcrRepo(Hook):

    def __init__(self, *args, **kwargs):
        super(CleanEcrRepo, self).__init__(*args, **kwargs)

    def run(self):

        if self.argument:
            region = self.stack.region
            repository_name = self.argument
            client = boto3.client('ecr', region_name=region)

            try:
                response = client.describe_images(repositoryName=repository_name)
                image_ids = []

                for imageDetail in response['imageDetails']:
                    image_ids.append(
                        {
                            'imageDigest': imageDetail['imageDigest'],
                        }
                    )

                    # Delete images if exist
                    if not len(image_ids):
                        print('No images to delete.')
                    else:
                        print('Starting images deletion...')
                        response = client.batch_delete_image(
                            repositoryName=repository_name,
                            imageIds=image_ids
                        )
                        print (response)

            except Exception as error_msg:
                if type(error_msg).__name__ == 'RepositoryNotFoundException':
                    print('Ecr {} repository does not exist on your region'.format(repository_name))
                else:
                    raise Exception("Error - Something bad happened - {}.".format(error_msg))
        else:
            raise Exception("Error - Expected Ecr Repository name argument.")
