# Build notes for the 'backend' container

  - The backend container is based on the image: registry.redhat.io/rhel9/python-311:latest.
  - It's stored at quay.io/dandavisredhat/potatofacts/backend and called in the compose file for the project.
  - Right now(10/13), it's just running sleep.py while I work out the Python calls to the db container.
  - When this dev work is complete, the entrypoint for backend will be the potatofacts app.
