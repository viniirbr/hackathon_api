## Run the frontend
1. Move to the hays-hackathon file
`cd man-city-hackathon-front-end/hays-hackathon`
2. Run the code with
`npm run start` with you are using NPM or `yarn start` if you are using Yarn

## Run the NestJS API
1. Move to the api file
`cd api`
2. Run the code with
`npm run start:dev` with you are using NPM or `yarn start:dev` if you are using Yarn

## Tracking energy API

The tracking energy API provides energy calculation from tracking data as well as energy predictions to inform coach decisions through the app.

### Running the API

To run this API locally you need to have Python 3.11 on your computer. 

- If you have make installed on your machine (default on Linux, see [here](https://stackoverflow.com/questions/2532234/how-to-run-a-makefile-in-windows) for Windows  and [here](https://stackoverflow.com/questions/10265742/how-to-install-make-and-gcc-on-a-mac) for Mac), then open a terminal on the tracking_energy_api folder and run make run. This will create a virtual environment in which requirements will be installed and the app will run on port 5000 of your localhost.
- Otherwise, open a terminal on the tracking_energy_api and run pip install -r requirements.txt, then run the tracking_energy_api\api\app.py python file either from an IDE or on the terminal by typing python api\app.py on the already open terminal. This should make the api run on the port 5000 of your localhost
