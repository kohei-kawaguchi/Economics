# LaTeX Writing Workflow

This document outlines the workflow for creating research papers and presentations using LaTeX templates.

## Templates

Two main templates are available:

1. `draft/draft.tex` - For academic papers and research drafts
2. `draft/slide.tex` - For presentations using Beamer

## Document Organization

**All documents should be placed in the `draft/` folder.**

This central location helps maintain consistency and makes it easier to:
- Apply common styling
- Share bibliographies
- Reuse figures across documents
- Track all writing projects in one place

## Draft Workflow

### Setup

1. Create a new file in the `draft/` directory with a descriptive name (e.g., `draft/paper_name.tex`)
2. Copy the content from `draft/draft.tex` as your starting template
3. Update the title, author, and abstract in the template

### Writing Process

1. Write your content in the main body of the document
2. Create figures in the `figuretable/` directory and reference them using:
   ```latex
   \begin{figure}[H]
       \centering
       \includegraphics[width=0.8\textwidth]{figuretable/your_figure.png}
       \caption{Your Caption}
   \end{figure}
   ```

3. Add citations by updating the `library.bib` file and using `\cite{key}`

### Compilation

Compile your document using XeLaTeX:
```
xelatex your_draft.tex
bibtex your_draft
xelatex your_draft.tex
xelatex your_draft.tex
```

## Presentation Workflow

### Setup

1. Create a new file in the `draft/` directory with a descriptive name (e.g., `draft/presentation_name.tex`)
2. Copy the content from `draft/slide.tex` as your starting template
3. Update the title, subtitle, author, and institute information

### Creating Slides

1. Organize your presentation with `\section{}` commands
2. Create new slides using the `\begin{frame}{Title}` environment
3. Use itemized lists, blocks, and columns as shown in the template

### Customization

The slide template includes HKUST colors by default:
- Navy blue (`hkustblue`): RGB(0, 51, 119)
- Golden brown (`hkustgold`): RGB(180, 141, 61)

You can customize colors by modifying the `\definecolor` commands.

### Compilation

Compile your presentation with:
```
xelatex your_slide.tex
```

## Compilation Environment

### Setup

This workflow uses:
- **TeXLive** distribution for LaTeX compilation
- **LaTeX Workshop** extension in VS Code/Cursor for editing and building

### VS Code/Cursor Setup and Workflow

1. Install the **LaTeX Workshop** extension in VS Code/Cursor
2. Open your LaTeX document
3. Build using the extension's commands:
   - Use the TeX icon in the sidebar to access build options
   - Press `Ctrl+Alt+B` (Windows/Linux) or `Cmd+Alt+B` (Mac) to build
   - Press `Ctrl+Alt+V` (Windows/Linux) or `Cmd+Alt+V` (Mac) to view PDF

4. Utilize LaTeX Workshop's powerful features:
   - SyncTeX: Ctrl+click (or Cmd+click) in the PDF to jump to source code
   - Snippets and IntelliSense for faster LaTeX writing
   - Error diagnostics in the Problems panel
   - Multi-file project support

### Magic Comments

The templates include magic comments at the top to help LaTeX Workshop:

```latex
% !TEX TS-program = xelatex
% !TEX TS-options = -synctex=1
```

These tell LaTeX Workshop to use XeLaTeX for compilation with SyncTeX support.

### Compilation Process

LaTeX Workshop handles the compilation sequence automatically:

- For drafts (with citations):
  1. XeLaTeX pass
  2. BibTeX pass
  3. XeLaTeX pass (resolve references)
  4. XeLaTeX pass (resolve cross-references)

- For presentations:
  1. XeLaTeX pass
  2. Additional passes if needed for references

You can also run these commands manually in the terminal if needed:

```
# For drafts with references
xelatex your_draft.tex
bibtex your_draft
xelatex your_draft.tex
xelatex your_draft.tex

# For presentations
xelatex your_slide.tex
```

## Tips and Best Practices

1. Use version control (Git) to track changes to your documents
2. Keep all papers and presentations in the `draft/` directory
3. Store shared figures in a common `figuretable/` directory
4. Maintain a single `library.bib` file for all your references
5. Use comments (`% comment`) to leave notes for yourself or collaborators
6. Use `\red{text}` and `\blue{text}` to highlight temporary notes or changes
