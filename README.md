# Canadian TV Simulator 2011

A Kivy-based Android application that simulates Canadian television channels from 2011 with programming guides, channel switching, and recording capabilities.

## Features

✅ **Canadian TV Channels**
- CBC News
- CTV News
- Global News
- City TV
- TSN Sports
- Sportsnet

✅ **Channel Management**
- Easy channel switching
- Channel numbering (1-6)
- Channel information display

✅ **Programming Guide**
- 2011 authentic TV programming schedules
- Program titles and duration
- Time-based scheduling

✅ **Recording Capability**
- Record programs with a single tap
- View recorded programs list
- Recording confirmation notifications

## Project Structure

```
canadian-tv-simulator/
├── main.py              # Main application file
├── buildozer.spec       # Buildozer configuration for APK
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- Java Development Kit (JDK)
- Android SDK
- Android NDK

### Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/papiceflomo353-alt/canadian-tv-simulator.git
   cd canadian-tv-simulator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally (Desktop):**
   ```bash
   python main.py
   ```

## Building APK

### Method 1: Using Buildozer (Recommended)

1. **Install Buildozer:**
   ```bash
   pip install buildozer
   ```

2. **Build the APK:**
   ```bash
   buildozer android debug
   ```

   For release build:
   ```bash
   buildozer android release
   ```

3. **APK Location:**
   - Debug: `bin/canadiantvSimulator-1.0-debug.apk`
   - Release: `bin/canadiantvSimulator-1.0-release.apk`

### Method 2: Using Docker (Alternative)

If you prefer a containerized approach:

```bash
docker run -it --rm -v $(pwd):/workspace ubuntu:20.04
cd /workspace
apt-get update && apt-get install -y python3 pip
pip install buildozer cython
buildozer android debug
```

## Usage

### Desktop Version
1. Run `python main.py`
2. Select a channel from the left panel
3. View the programming guide in the center
4. Click any program to record it
5. View recordings on the right panel

### Mobile Version
1. Install the APK on your Android device
2. Launch the app
3. Same functionality as desktop version

## 2011 Programming Guide

### CBC (Channel 1)
- 08:00 - CBC News Morning (120 min)
- 10:00 - The National (60 min)
- 18:00 - CBC News at 6 (30 min)
- 22:00 - CBC News at 11 (30 min)

### CTV (Channel 2)
- 07:00 - Canada AM (180 min)
- 17:00 - CTV News at 5 (60 min)
- 18:00 - CTV National News (30 min)
- 23:00 - CTV News at 11 (30 min)

### Global (Channel 3)
- 06:00 - Sunrise (180 min)
- 17:00 - Global News Hour (60 min)
- 18:00 - Global News at 6 (30 min)
- 23:00 - Global News at 11 (30 min)

### City TV (Channel 4)
- 09:00 - Breakfast Television (180 min)
- 12:00 - Midday Show (60 min)
- 17:00 - City News at 5 (60 min)
- 22:00 - City News at 10 (30 min)

### TSN (Channel 5)
- 10:00 - SportsCentre (60 min)
- 14:00 - NHL Hockey (180 min)
- 19:00 - CFL Football (180 min)
- 22:00 - SportsCentre Late (60 min)

### Sportsnet (Channel 6)
- 11:00 - Headlines (30 min)
- 15:00 - Blue Jays Game (180 min)
- 20:00 - Hockey Game (180 min)
- 23:00 - Highlights (60 min)

## Technical Details

### Built With
- **Kivy** - Python UI framework for Android
- **Python 3** - Programming language
- **Buildozer** - Build system for Python Android apps

### System Requirements
- Android 5.0+ (API 21+)
- Minimum 50MB storage space
- Touch screen device

## Development

### Adding New Channels

Edit the `CHANNELS` dictionary in `main.py`:

```python
CHANNELS = {
    'YourChannel': {
        'name': 'Channel Name',
        'number': 7,
        'logo': 'assets/channel_logo.png',
        'programs': [
            {'time': 'HH:MM', 'title': 'Program Title', 'duration': 'XX min'},
            # More programs...
        ]
    }
}
```

### Customizing the UI

Modify the `build()` method in the `CanadianTVSimulator` class to adjust:
- Layout colors
- Font sizes
- Widget spacing
- Button styles

## Troubleshooting

### APK Build Fails
1. Ensure all prerequisites are installed
2. Update Android SDK and NDK
3. Clear build cache: `buildozer android clean`

### App Crashes on Mobile
1. Check logcat: `adb logcat`
2. Verify permissions in `buildozer.spec`
3. Test on different Android versions

### Recordings Not Persisting
Currently, recordings are stored in memory. To add persistence:
1. Implement SQLite database
2. Add file system storage
3. Create backup/restore functionality

## Future Enhancements

- [ ] Persistent recording storage
- [ ] Channel custom favorites
- [ ] DVR-like playback functionality
- [ ] EPG (Electronic Program Guide) import
- [ ] Multi-day programming schedules
- [ ] User preferences/settings
- [ ] Dark mode UI
- [ ] Notifications for upcoming programs

## License

MIT License - Feel free to use this project for personal or commercial purposes.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed descriptions

## Support

For issues or questions:
1. Check existing GitHub issues
2. Create a new issue with detailed information
3. Include device specs and error messages

---

**Created:** 2026
**Last Updated:** May 30, 2026
**Version:** 1.0
