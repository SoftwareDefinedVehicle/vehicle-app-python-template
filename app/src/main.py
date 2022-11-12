# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

"""A sample skeleton vehicle app."""

# pylint: disable=C0103, C0413, E1101

import asyncio
import json
import logging
import signal

from sdv.util.log import (  # type: ignore
    get_opentelemetry_log_factory,
    get_opentelemetry_log_format,
)
from sdv.vdb.subscriptions import DataPointReply
from sdv.vehicle_app import VehicleApp, subscribe_topic
from sdv_model import Vehicle, vehicle  # type: ignore
import digital_auto_compat #type: ignore

# Configure the VehicleApp logger with the necessary log config and level.
logging.setLogRecordFactory(get_opentelemetry_log_factory())
logging.basicConfig(format=get_opentelemetry_log_format())
logging.getLogger().setLevel("DEBUG")
logger = logging.getLogger(__name__)

GET_SPEED_REQUEST_TOPIC = "sampleapp/getSpeed"
GET_SPEED_RESPONSE_TOPIC = "sampleapp/getSpeed/response"
DATABROKER_SUBSCRIPTION_TOPIC = "sampleapp/currentSpeed"


class SampleApp(VehicleApp):
    """
    Sample skeleton vehicle app.

    The skeleton subscribes to a getSpeed MQTT topic
    to listen for incoming requests to get
    the current vehicle speed and publishes it to
    a response topic.

    It also subcribes to the VehicleDataBroker
    directly for updates of the
    Vehicle.Speed signal and publishes this
    information via another specific MQTT topic
    """

    def __init__(self, vehicle_client: Vehicle):
        # SampleApp inherits from VehicleApp.
        super().__init__()
        self.Vehicle = vehicle_client

    async def on_start(self):
        profile = {
            "standard": {
                "BackrestLumbarHeight": 0,
                "HeadrestAngle": 0,
                "Positon": 0,
                "Height": 0,
            },
            "user": {
                "BackrestLumbarHeight": 20,
                "HeadrestAngle": 10,
                "Positon": 42,
                "Height": 10,
            },
        }

        PrevProfileId = 1

        async def on_user_profile_changed(Issuer: str):
            print("Listener was triggered")
            if PrevProfileId != Issuer:
                await self.Vehicle.Cabin.Seat.Row1.Pos1.Height.set(
                    profile[Issuer]["VerticalHeight"]
                )
                await self.Vehicle.Cabin.Seat.Row1.Pos1.Position.set(
                    profile[Issuer]["HorizontalPosition"]
                )

        await self.Vehicle.Cabin.Seat.Row1.Pos1.Position.subscribe(
            on_user_profile_changed
        )
        print("Listener was registered")

        # Now test the listener
        print("Changing user profile")
        BackrestLumbarHeight = (
            await vehicle.Cabin.Seat.Row1.Pos1.Backrest.Lumbar.Height.get()
        )
        HeadrestAngle = await vehicle.Cabin.Seat.Row1.Pos1.Headrest.Angle.get()
        Positon = await vehicle.Cabin.Seat.Row1.Pos1.Position.get()
        Height = await vehicle.Cabin.Seat.Row1.Pos1.Height.get()

        print("Lumbar Height", BackrestLumbarHeight)
        print("Headrest Angle", HeadrestAngle)
        print("Position", Positon)
        print("Height", Height)

        print("Changing user profile")
        BackrestLumbarHeight = (
            await vehicle.Cabin.Seat.Row1.Pos1.Backrest.Lumbar.Height.get()
        )
        HeadrestAngle = await vehicle.Cabin.Seat.Row1.Pos1.Headrest.Angle.get()
        Positon = await vehicle.Cabin.Seat.Row1.Pos1.Position.get()
        Height = await vehicle.Cabin.Seat.Row1.Pos1.Height.get()

        print("Lumbar Height", BackrestLumbarHeight)
        print("Headrest Angle", HeadrestAngle)
        print("Position", Positon)
        print("Height", Height)


async def main():

    """Main function"""
    logger.info("Starting SampleApp...")
    # Constructing SampleApp and running it.
    vehicle_app = SampleApp(vehicle)
    await vehicle_app.run()


LOOP = asyncio.get_event_loop()
LOOP.add_signal_handler(signal.SIGTERM, LOOP.stop)
LOOP.run_until_complete(main())
LOOP.close()
