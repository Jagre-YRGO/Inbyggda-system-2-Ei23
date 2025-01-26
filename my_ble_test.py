import asyncio
from bleak import BleakScanner, BleakClient

print('starting BLE test...')

client = None
address = "A4:06:E9:79:FB:8B"
CUSTOM_CHAR_UUID = '0000FFE1-0000-1000-8000-00805F9B34FB'


async def main():
    global client

    async with BleakClient(address) as client:
        while True:
            char = input('turn on/off: ')
            if char == '1':
                await client.write_gatt_char(CUSTOM_CHAR_UUID, b'1')
            elif char == '0':
                await client.write_gatt_char(CUSTOM_CHAR_UUID, b'0')
            else:
                await client.disconnect()
                break;
            

if __name__ == "__main__":
    asyncio.run(main())
    print('ending BLE test...')
