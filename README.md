# System Cleaner

A modern, user-friendly system cleaning utility built with Python and CustomTkinter. This application helps you free up disk space by clearing temporary files and emptying the recycle bin with a sleek dark-themed GUI.

![DEV](https://img.shields.io/badge/Dev-Bojidar%20Georgiev%20-%20%2347b3ff)
![System Cleaner Interface](https://img.shields.io/badge/GUI-CustomTkinter-blue)
![Python Version](https://img.shields.io/badge/Python-3.7+-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

## Features

- **Clear Temporary Files**: Removes files from the system's temporary directory (`%temp%`)
- **Empty Recycle Bin**: Safely empties the Windows recycle bin
- **Real-time Progress**: Visual progress bar and status updates
- **Space Calculation**: Shows how much disk space was freed
- **Modern UI**: Dark-themed interface with CustomTkinter
- **Threading**: Non-blocking operations that keep the UI responsive
- **Error Handling**: Graceful handling of permission errors and edge cases

## Screenshots

The application features a clean, modern interface with:
- Dark theme with blue accent colors
- Large, easy-to-click buttons
- Real-time status updates
- Progress bar for ongoing operations

## Requirements

- Python 3.7 or higher
- Windows operating system
- CustomTkinter library

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BGeorgiev120/Clear-Away
   ```

2. **Install required dependencies:**
   ```bash
   pip install customtkinter
   ```

3. **Optional: Add application icon**
   - Place an `open-folder.ico` file in the same directory as `main.py` for a custom window icon
   - The application will work without this file

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Using the features:**
   - **Clear Temp Data**: Click to remove temporary files and see how much space was freed
   - **Clear Recycle Bin**: Click to empty the recycle bin completely
   - Monitor the status label and progress bar for operation updates

3. **Best Practices:**
   - Run as administrator for best results (especially for recycle bin operations)
   - Close other applications before cleaning for optimal performance
   - Review the success messages to see how much space was freed

## How It Works

### Temporary File Cleaning
- Scans the system's temporary directory (`%temp%`)
- Safely removes files and empty directories
- Calculates and reports freed disk space
- Handles permission errors gracefully

### Recycle Bin Cleaning
- Uses PowerShell's `Clear-RecycleBin` command as the primary method
- Falls back to direct file system operations if needed
- Works across multiple drives
- Provides detailed feedback on the operation

## Technical Details

- **GUI Framework**: CustomTkinter for modern, themed interface
- **Threading**: Uses daemon threads to prevent UI blocking
- **Error Handling**: Comprehensive exception handling for file operations
- **Cross-Drive Support**: Handles multiple drive letters for recycle bin cleaning
- **Memory Efficient**: Processes files iteratively to handle large directories

## Safety Features

- **Permission Handling**: Skips files that can't be deleted due to permissions
- **Non-Destructive**: Only removes temporary files and recycle bin contents
- **User Feedback**: Clear success/error messages
- **Button States**: Buttons are disabled during operations to prevent conflicts

## Troubleshooting

### Common Issues

1. **"Required packages not found" error:**
   ```bash
   pip install customtkinter
   ```

2. **Permission denied errors:**
   - Run the application as administrator
   - Some system files may be in use and cannot be deleted

3. **Icon file warning:**
   - This is harmless - the app works without the icon file
   - Add `open-folder.ico` to remove the warning

4. **Incomplete recycle bin operation:**
   - Try running as administrator
   - Some files may be in use by other applications

## Contributing

Contributions are welcome! Here are some ways you can help:

1. **Bug Reports**: Open an issue with details about any bugs you find
2. **Feature Requests**: Suggest new cleaning features or UI improvements
3. **Code Contributions**: Submit pull requests with improvements
4. **Documentation**: Help improve this README or add code comments

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly on Windows
5. Submit a pull request

## Future Enhancements

- [ ] Browser cache cleaning
- [ ] Registry cleaning
- [ ] Scheduled cleaning
- [ ] Custom folder selection
- [ ] Detailed cleaning reports
- [ ] Settings/preferences panel
- [ ] Multi-language support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky
- Icon design inspiration from modern file management applications
- Thanks to the Python community for excellent documentation and support

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/system-cleaner/issues) page
2. Create a new issue with:
   - Your Python version
   - Windows version
   - Error messages (if any)
   - Steps to reproduce the problem

---

**Note**: This application is designed for Windows systems. Always ensure you have backups of important data before running any system cleaning operations.
