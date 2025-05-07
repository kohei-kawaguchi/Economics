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

## Figure and Table Management

### Programmatic Generation

All figures and tables in the `figuretable/` directory **must be programmatically generated** and should **never be manually edited**. This ensures:

- Reproducibility of results
- Consistency across revisions
- Proper version control of data visualizations

### Generation Scripts

Scripts for generating figures and tables must be placed in the `report/` folder:

- **R**: Use Rmarkdown (.Rmd) or Quarto (.qmd) files
- **Python**: Use Jupyter notebooks (.ipynb) or scripts (.py)
- **Stata**: Use .do files with export commands

Example R workflow using Rmarkdown/Quarto:
```r
# In report/generate_figures.Rmd or report/generate_figures.qmd
library(ggplot2)
library(dplyr)

# Load data
data <- read.csv("data/your_dataset.csv")

# Create figure
p <- 
   ggplot(
      data, 
      aes(
         x = x_variable, 
         y = y_variable
      )
   ) +
  geom_point() +
  theme_classic() +
  labs(
   title = "Your Title"
  )

# Save to figuretable directory
ggsave(
   "../figuretable/your_figure.png", 
   p, 
   width = 8, 
   height = 6
)
```

### Workflow

1. Create scripts in the `report/` directory using Rmarkdown, Quarto, or other reproducible formats
2. Write code to generate visualizations and tables within these scripts
3. Run scripts to output results directly to the `figuretable/` directory
4. Reference these outputs in your LaTeX documents

### Referencing in LaTeX

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{figuretable/your_programmatically_generated_figure.png}
    \caption{Caption describing the programmatically generated figure}
\end{figure}
```

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
3. Store only programmatically generated figures and tables in the `figuretable/` directory
4. Generate all figures and tables using reproducible scripts in the `report/` folder
5. Maintain a single `library.bib` file for all your references
6. DO NOT use comments (`% comment`) to leave notes for yourself or collaborators
7. DO NOT use `\red{text}` and `\blue{text}` to highlight temporary notes or changes
