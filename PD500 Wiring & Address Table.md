### RS485 Output Wiring

| Wire Color | Function                  |
|------------|---------------------------|
| Red        | Power Positive (VCC)      |
| Green      | Ground (GND)              |
| Yellow     | RS485A (Pressure + Temp)  |
| Blue       | RS485B (Pressure + Temp)  |
| Black      | Shield Ground (PE)        |


### RS485 Address Table
| Function                | Hex Address     | Decimal Address | Type       | Notes               |
|-------------------------|-----------------|-----------------|------------|---------------------|
| Device Address          | `0x0000`        | `0`             | UINT16     | Slave ID            |
| Baud Rate               | `0x0001`        | `1`             | UINT16     | Serial baud setting |
| Unit                    | `0x0002`        | `2`             | UINT16     | kPa, MPa, bar, etc  |
| Decimal Offset          | `0x0003`        | `3`             | UINT16     | Scaling factor      |
| Pressure Value (INT)    | `0x0004`        | `4`             | INT16      | Raw pressure        |
| Linear Correction       | `0x0005`        | `5`             | INT16      | Calibration         |
| Zero Offset             | `0x0006`        | `6`             | INT16      | Zero calibration    |
| Density                 | `0x0007`        | `7`             | UINT16     | Density setting     |
| Parity                  | `0x0008`        | `8`             | UINT16     | None/Odd/Even       |
| Temperature Value (INT) | `0x0014`        | `20`            | UINT16     | Raw temp ×0.1       |
| Temperature Float       | `0x0022~0x0023` | `34~35`         | FLOAT CDAB | Recommended         |
| Pressure Float          | `0x0024~0x0025` | `36~37`         | FLOAT CDAB | Recommended         |
| Save Settings           | `0x001F`        | `31`            | UINT16     | Write `0x001F`      |