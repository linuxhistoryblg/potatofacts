# catfacts
A re-implementation of catfacts using podman
![functional diagram](functional_diagram.png)


The goal of this hobby project will be to gain a better understanding of creating and running a 'composed' podman application.

The application will be a reimplementation of the catfacts prank [featured on Reddit](https://www.reddit.com/r/funny/comments/owx3v/so_my_little_cousin_posted_on_fb_that_he_was/).

The app will consist of a Mariadb database to hold subscriber information and facts about cats, a python backend to take new subscriptions and serve catfacts from the database. It will interface with an SMS gateway that will enable it to send cat facts to SMS subscribers.

## TODO:
  - [x] Identify and test a podman container-image suitable for the project goals
  - [ ] Define the database tables necessary for the project
  - [x] Identify a podman container-image suitable for running the backent
  - [ ] Write the backend python to take subscription requests, serve cat facts, and interface with the SMS gateway
  - [ ] Rent time on an SMS gateway provider
  - [ ] Create a podman-compose file to start both containers together
  - [ ] QA/UAT
  - [ ] RELEASE
