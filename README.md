# DVIR Form Reviewer

A web-based tool for reviewing and annotating AI-generated DVIR (Driver Vehicle Inspection Report) forms.

## Features

- **Review Multiple Forms**: Navigate through various DVIR form variations (different vehicle types and compliance levels)
- **Combined Annotations**: Create annotations with any combination of:
  - Form item selection
  - Error tag categorization
  - Text comments
- **Multiple Annotations**: Add multiple separate annotations to the same form item
- **Visual Feedback**: Clear indicators showing which items have annotations and how many
- **Export Options**: Export annotations in JSON or CSV format
- **Progress Tracking**: Track review progress across all forms
- **Local Storage**: Annotations persist in browser localStorage
- **Clear Data**: Reset all annotations to start fresh

## Getting Started

### Requirements

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Local web server (Python, Node.js, or any HTTP server)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/catalinviciu/DVIR_Form_Reviewer.git
   cd DVIR_Form_Reviewer
   ```

2. Start a local web server:
   ```bash
   # Using Python 3
   python -m http.server 8000

   # Or using Node.js (if you have http-server installed)
   npx http-server -p 8000
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8000/review.html
   ```

## Usage

### Reviewing Forms

1. **Navigate**: Use "Previous" and "Next" buttons or arrow keys to move between forms
2. **Progress**: Track your progress in the header (shows current form and review completion percentage)

### Adding Annotations

You can create annotations with any combination of these components:

1. **Select a Form Item**: Click any inspection item in the left panel
2. **Choose an Error Tag**: Select from predefined error categories (Missing Item, Wrong Terminology, etc.)
3. **Add a Comment**: Type any text note in the comment box

All selected components will combine into a single annotation when you click "Add Annotation".

**Example**:
- Click "Form Item #1: Front Photo"
- Select "Insufficient Detail" error tag
- Type "Photo is too blurry to see damage"
- Click "Add Annotation"

This creates ONE annotation with all three components.

### Multiple Annotations

You can add multiple separate annotations to the same form item. Each annotation is tracked independently and displayed in the annotations list.

### Exporting Data

1. Click the **"Export Annotations"** button
2. Choose your preferred format:
   - **JSON**: Full structured data, ideal for backup or programmatic processing
   - **CSV**: Spreadsheet-ready format, opens directly in Excel or Google Sheets
3. Click **"Export"** to download the file

### Clearing Data

Click the **"Clear All Data"** button (red button) to remove all annotations from localStorage and start fresh. This action requires confirmation and cannot be undone.

## Keyboard Shortcuts

- **Left Arrow**: Previous form
- **Right Arrow**: Next form
- **S**: Save current annotation (when selection is active)

## Data Structure

### Annotations Storage

Annotations are stored in the following structure:

```json
{
  "filename.json": [
    {
      "formItem": {
        "itemIndex": 0,
        "itemName": "Headlights (both)",
        "itemType": "Checkbox"
      },
      "errorTag": "Insufficient Detail",
      "comment": "Left headlight is dimmer than right",
      "timestamp": "2025-10-20T13:45:30.123Z"
    }
  ]
}
```

### CSV Export Format

| Filename | Form Item Index | Form Item Name | Form Item Type | Error Tag | Comment | Timestamp |
|----------|----------------|----------------|----------------|-----------|---------|-----------|
| form.json | 0 | Headlights (both) | Checkbox | Insufficient Detail | Left headlight dim | 2025-10-20T... |

## Sample Forms

The tool includes sample DVIR forms for:

**Vehicles:**
- Chevrolet Silverado
- Skoda Kamiq

**Variations:**
- With/without maintenance items
- Minimum vs. extended compliance levels

## Technology

- Pure HTML/CSS/JavaScript
- No external dependencies
- Browser localStorage for persistence
- Client-side only (no server required)

## License

This project is open source and available for review and evaluation purposes.

## Contributing

Issues and pull requests are welcome!

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
