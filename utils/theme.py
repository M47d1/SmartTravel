"""
SmartTravel - Theme & Style Constants
Palet warna dan stylesheet global berbasis desain travel premium.
"""

# ── Color Palette ────────────────────────────────────────────────────────────
PRIMARY        = "#0A2342"   # navy deep
SECONDARY      = "#1565C0"   # ocean blue
ACCENT         = "#FF6B35"   # sunset orange
ACCENT_HOVER   = "#E55A25"
BG_DARK        = "#0D1B2A"
BG_MEDIUM      = "#1B2A3B"
BG_CARD        = "#1E3A5F"
BG_INPUT       = "#162435"
TEXT_PRIMARY   = "#F0F4F8"
TEXT_SECONDARY = "#8EADC1"
TEXT_MUTED     = "#4A6B80"
SUCCESS        = "#2ECC71"
WARNING        = "#F39C12"
DANGER         = "#E74C3C"
BORDER         = "#1E3A5F"
SIDEBAR_W      = 220

MAIN_STYLE = f"""
/* ── Global ── */
QWidget {{
    background-color: {BG_DARK};
    color: {TEXT_PRIMARY};
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 13px;
}}

/* ── QLineEdit / QTextEdit ── */
QLineEdit, QTextEdit, QComboBox, QSpinBox, QDateEdit {{
    background-color: {BG_INPUT};
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 8px 12px;
    color: {TEXT_PRIMARY};
    selection-background-color: {SECONDARY};
}}
QLineEdit:focus, QTextEdit:focus, QComboBox:focus,
QSpinBox:focus, QDateEdit:focus {{
    border: 1px solid {SECONDARY};
}}

/* ── QPushButton ── */
QPushButton {{
    background-color: {SECONDARY};
    color: white;
    border: none;
    border-radius: 6px;
    padding: 9px 20px;
    font-weight: 600;
    letter-spacing: 0.3px;
}}
QPushButton:hover  {{ background-color: #1976D2; }}
QPushButton:pressed{{ background-color: #0D47A1; }}
QPushButton#btnAccent {{
    background-color: {ACCENT};
}}
QPushButton#btnAccent:hover {{
    background-color: {ACCENT_HOVER};
}}
QPushButton#btnDanger {{
    background-color: {DANGER};
}}
QPushButton#btnDanger:hover {{
    background-color: #C0392B;
}}
QPushButton#btnSuccess {{
    background-color: {SUCCESS};
    color: #0D1B2A;
}}
QPushButton#btnGhost {{
    background-color: transparent;
    color: {TEXT_SECONDARY};
    border: 1px solid {BORDER};
}}
QPushButton#btnGhost:hover {{
    background-color: {BG_MEDIUM};
    color: {TEXT_PRIMARY};
}}

/* ── QTableWidget ── */
QTableWidget {{
    background-color: {BG_MEDIUM};
    border: none;
    gridline-color: {BORDER};
    border-radius: 8px;
    alternate-background-color: {BG_CARD};
}}
QTableWidget::item {{
    padding: 8px 12px;
    border: none;
}}
QTableWidget::item:selected {{
    background-color: {SECONDARY};
    color: white;
}}
QHeaderView::section {{
    background-color: {PRIMARY};
    color: {TEXT_SECONDARY};
    padding: 10px 12px;
    border: none;
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}}

/* ── QScrollBar ── */
QScrollBar:vertical {{
    background: {BG_DARK};
    width: 8px;
    border-radius: 4px;
}}
QScrollBar::handle:vertical {{
    background: {TEXT_MUTED};
    border-radius: 4px;
    min-height: 30px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}

/* ── QTabWidget ── */
QTabWidget::pane {{
    border: 1px solid {BORDER};
    border-radius: 8px;
    background: {BG_MEDIUM};
}}
QTabBar::tab {{
    background: {BG_DARK};
    color: {TEXT_SECONDARY};
    padding: 10px 20px;
    margin-right: 2px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
}}
QTabBar::tab:selected {{
    background: {SECONDARY};
    color: white;
    font-weight: 600;
}}

/* ── QMessageBox ── */
QMessageBox {{
    background-color: {BG_MEDIUM};
}}
QMessageBox QLabel {{
    color: {TEXT_PRIMARY};
}}

/* ── QLabel ── */
QLabel#titleLabel {{
    font-size: 20px;
    font-weight: 700;
    color: {TEXT_PRIMARY};
}}
QLabel#subtitleLabel {{
    font-size: 13px;
    color: {TEXT_SECONDARY};
}}
QLabel#sectionLabel {{
    font-size: 11px;
    font-weight: 700;
    color: {TEXT_MUTED};
    text-transform: uppercase;
    letter-spacing: 1px;
}}
"""

SIDEBAR_STYLE = f"""
QWidget#sidebar {{
    background-color: {PRIMARY};
    border-right: 1px solid #0D1F35;
}}
QPushButton#navBtn {{
    background: transparent;
    color: {TEXT_SECONDARY};
    border: none;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: left;
    font-size: 13px;
    font-weight: 500;
}}
QPushButton#navBtn:hover {{
    background-color: rgba(21,101,192,0.3);
    color: {TEXT_PRIMARY};
}}
QPushButton#navBtn:checked {{
    background-color: {SECONDARY};
    color: white;
    font-weight: 600;
}}
"""

LOGIN_STYLE = f"""
QWidget {{
    background-color: {BG_DARK};
    color: {TEXT_PRIMARY};
    font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
}}
QLineEdit {{
    background-color: {BG_INPUT};
    border: 1px solid {BORDER};
    border-radius: 8px;
    padding: 12px 16px;
    color: {TEXT_PRIMARY};
    font-size: 14px;
}}
QLineEdit:focus {{
    border: 1px solid {SECONDARY};
}}
QPushButton#btnLogin {{
    background-color: {ACCENT};
    color: white;
    border: none;
    border-radius: 8px;
    padding: 13px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.5px;
}}
QPushButton#btnLogin:hover {{
    background-color: {ACCENT_HOVER};
}}
QPushButton#btnLogin:pressed {{
    background-color: #C84D20;
}}
"""
