import argparse
import asyncio
from bitcoin_value import currency
    
from govee_api_laggat import Govee


async def foo(api_key):
    INTERVAL = 20 # Interval how many seconds pass between each measurement
    PricePast = currency("EUR") # Measures First price point

    # this is for testing bug #72
    async with Govee(api_key) as govee:
        devices, err = await govee.get_devices() # Fill an array containing all your Govee devices
        while True:
            blue = 0; # Blue color stays 0 the whole time
            await asyncio.sleep(INTERVAL) # Wait duration of INTERVAL
            PriceNow = currency("EUR") #Measures price after waiting
            PriceDifference = PriceNow - PricePast #Price difference to determine gain or loss
            print(PriceNow, PricePast, PriceDifference) 
            PricePast = PriceNow # Current Price will be compared to future price
            if PriceDifference > 0:
                green = 255
                red = 0
            else:
                green = 0
                red = 255

            for dev in devices: # Do this for each device found on your account
                # turn and set color
                success, err = await govee.set_color(dev, (red, green, blue))
                print("set")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="govee_api_laggat examples")
    parser.add_argument("--api-key", dest="api_key", type=str, required=True)
    args = parser.parse_args()

    # going async ...
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(foo(args.api_key))
    finally:
        loop.close()
