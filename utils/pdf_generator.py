"""
SmartTravel - Invoice PDF Generator
Menghasilkan invoice PDF profesional menggunakan ReportLab.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph,
    Spacer, HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from datetime import datetime
import os
from pathlib import Path


# Warna brand
NAVY    = colors.HexColor("#0A2342")
BLUE    = colors.HexColor("#1565C0")
ORANGE  = colors.HexColor("#FF6B35")
LGRAY   = colors.HexColor("#F0F4F8")
MGRAY   = colors.HexColor("#8EADC1")
WHITE   = colors.white
BLACK   = colors.HexColor("#0D1B2A")

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "database" / "invoices"


def generate_invoice(transaksi, pelanggan, paket) -> str:
    """
    Membuat file PDF invoice dan mengembalikan path file.

    Parameters
    ----------
    transaksi : Transaksi dataclass
    pelanggan : Pelanggan dataclass
    paket     : PaketWisata dataclass

    Returns
    -------
    str – absolute path ke file PDF yang dihasilkan
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = OUTPUT_DIR / f"{transaksi.kode_invoice}.pdf"

    doc = SimpleDocTemplate(
        str(filename),
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()
    story = []

    # ── Header ──────────────────────────────────────────────────────────────
    header_data = [[
        Paragraph(
            '<font color="#FF6B35" size="26"><b>Smart</b></font>'
            '<font color="#F0F4F8" size="26"><b>Travel</b></font><br/>'
            '<font color="#8EADC1" size="9">Sistem Manajemen Reservasi & Paket Wisata</font>',
            ParagraphStyle("h", backColor=NAVY),
        ),
        Paragraph(
            f'<font color="#F0F4F8" size="22"><b>INVOICE</b></font><br/>'
            f'<font color="#8EADC1" size="9">{transaksi.kode_invoice}</font>',
            ParagraphStyle("inv", alignment=TA_RIGHT, backColor=NAVY),
        ),
    ]]
    header_tbl = Table(header_data, colWidths=[10 * cm, 7 * cm])
    header_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("TEXTCOLOR",  (0, 0), (-1, -1), WHITE),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 18),
        ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ("TOPPADDING",   (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 18),
        ("ROUNDEDCORNERS", (0,0), (-1,-1), [8,8,8,8]),
    ]))
    story.append(header_tbl)
    story.append(Spacer(1, 0.6 * cm))

    # ── Meta info: Tanggal & Status ──────────────────────────────────────────
    status_color = {"Confirmed": "#2ECC71", "Pending": "#F39C12", "Cancelled": "#E74C3C"}.get(
        transaksi.status, "#8EADC1"
    )
    meta_data = [[
        Paragraph(
            f'<font color="#4A6B80" size="9">TANGGAL INVOICE</font><br/>'
            f'<font color="#0D1B2A" size="11"><b>{transaksi.tanggal_pesan}</b></font>',
            styles["Normal"],
        ),
        Paragraph(
            f'<font color="#4A6B80" size="9">TANGGAL CETAK</font><br/>'
            f'<font color="#0D1B2A" size="11"><b>{datetime.now().strftime("%d %B %Y")}</b></font>',
            styles["Normal"],
        ),
        Paragraph(
            f'<font color="#4A6B80" size="9">STATUS</font><br/>'
            f'<font color="{status_color}" size="12"><b>{transaksi.status}</b></font>',
            styles["Normal"],
        ),
    ]]
    meta_tbl = Table(meta_data, colWidths=[6 * cm, 6 * cm, 5 * cm])
    meta_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
        ("ROUNDEDCORNERS", (0,0), (-1,-1), [6,6,6,6]),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 0.6 * cm))

    # ── Billing To ──────────────────────────────────────────────────────────
    bill_style = ParagraphStyle("bill", fontSize=10, leading=16, textColor=BLACK)
    bill_data = [[
        _section_block("TAGIHAN KEPADA",
                       f"<b>{pelanggan.nama}</b><br/>"
                       f"{pelanggan.email or '-'}<br/>"
                       f"Telp: {pelanggan.telepon or '-'}<br/>"
                       f"{pelanggan.alamat or '-'}"),
        _section_block("DITERBITKAN OLEH",
                       "<b>SmartTravel Agency</b><br/>"
                       "admin@smarttravel.id<br/>"
                       "Telp: +62 800-SMART-TV<br/>"
                       "Indonesia"),
    ]]
    bill_tbl = Table(bill_data, colWidths=[8.5 * cm, 8.5 * cm])
    bill_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(bill_tbl)
    story.append(Spacer(1, 0.5 * cm))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1E3A5F")))
    story.append(Spacer(1, 0.4 * cm))

    # ── Detail Paket ─────────────────────────────────────────────────────────
    item_headers = [
        Paragraph('<font color="white" size="9"><b>DESKRIPSI PAKET</b></font>', styles["Normal"]),
        Paragraph('<font color="white" size="9"><b>DURASI</b></font>', styles["Normal"]),
        Paragraph('<font color="white" size="9"><b>HARGA/PAX</b></font>', styles["Normal"]),
        Paragraph('<font color="white" size="9"><b>PAX</b></font>', styles["Normal"]),
        Paragraph('<font color="white" size="9"><b>SUBTOTAL</b></font>', styles["Normal"]),
    ]
    harga_per_orang = paket.harga
    subtotal = harga_per_orang * transaksi.jumlah_orang

    item_row = [
        Paragraph(
            f'<b>{paket.nama_paket}</b><br/>'
            f'<font color="#4A6B80" size="9">Destinasi: {paket.destinasi}</font>',
            styles["Normal"],
        ),
        f"{paket.durasi_hari} Hari",
        f"Rp {harga_per_orang:,.0f}",
        str(transaksi.jumlah_orang),
        Paragraph(f'<b>Rp {subtotal:,.0f}</b>', styles["Normal"]),
    ]

    item_tbl = Table(
        [item_headers, item_row],
        colWidths=[6.5 * cm, 2 * cm, 3 * cm, 1.5 * cm, 3.5 * cm],
    )
    item_tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR",    (0, 0), (-1, 0), WHITE),
        ("FONTSIZE",     (0, 0), (-1, 0), 9),
        ("TOPPADDING",   (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 10),
        ("LEFTPADDING",  (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("BACKGROUND",   (0, 1), (-1, 1), LGRAY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LGRAY, WHITE]),
        ("GRID",         (0, 0), (-1, -1), 0.5, colors.HexColor("#1E3A5F")),
        ("ALIGN",        (1, 0), (-1, -1), "CENTER"),
        ("ALIGN",        (4, 0), (4, -1), "RIGHT"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(item_tbl)
    story.append(Spacer(1, 0.4 * cm))

    # ── Total ────────────────────────────────────────────────────────────────
    total_data = [
        ["", "Subtotal", f"Rp {subtotal:,.0f}"],
        ["", "Pajak (0%)", "Rp 0"],
        ["", Paragraph('<b>TOTAL</b>', styles["Normal"]),
         Paragraph(f'<font color="#FF6B35" size="14"><b>Rp {transaksi.total_harga:,.0f}</b></font>',
                   styles["Normal"])],
    ]
    total_tbl = Table(total_data, colWidths=[9.5 * cm, 3.5 * cm, 4 * cm])
    total_tbl.setStyle(TableStyle([
        ("ALIGN",        (1, 0), (-1, -1), "RIGHT"),
        ("TOPPADDING",   (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 7),
        ("LEFTPADDING",  (1, 0), (-1, -1), 10),
        ("RIGHTPADDING", (2, 0), (-1, -1), 10),
        ("LINEABOVE",    (1, 2), (-1, 2), 1.5, NAVY),
        ("BACKGROUND",   (1, 2), (-1, 2), LGRAY),
        ("FONTSIZE",     (0, 0), (-1, -1), 10),
    ]))
    story.append(total_tbl)
    story.append(Spacer(1, 0.5 * cm))

    # ── Catatan & Info Keberangkatan ─────────────────────────────────────────
    if transaksi.tanggal_berangkat:
        story.append(Paragraph(
            f'<font color="#4A6B80" size="9">TANGGAL KEBERANGKATAN</font><br/>'
            f'<font color="#0A2342" size="12"><b>{transaksi.tanggal_berangkat}</b></font>',
            styles["Normal"],
        ))
        story.append(Spacer(1, 0.3 * cm))

    if transaksi.catatan:
        story.append(Paragraph(
            f'<font color="#4A6B80" size="9">CATATAN</font><br/>{transaksi.catatan}',
            ParagraphStyle("note", fontSize=10, textColor=BLACK),
        ))
        story.append(Spacer(1, 0.3 * cm))

    # ── Footer ───────────────────────────────────────────────────────────────
    story.append(Spacer(1, 0.8 * cm))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1E3A5F")))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        '<font color="#8EADC1" size="9">Terima kasih telah mempercayai SmartTravel. '
        'Invoice ini diterbitkan secara digital dan sah tanpa tanda tangan basah. '
        'Hubungi kami di admin@smarttravel.id untuk pertanyaan lebih lanjut.</font>',
        ParagraphStyle("footer", alignment=TA_CENTER, fontSize=9),
    ))

    doc.build(story)
    return str(filename)


def _section_block(title: str, content: str) -> Paragraph:
    styles = getSampleStyleSheet()
    html = (
        f'<font color="#4A6B80" size="9"><b>{title}</b></font><br/>'
        f'<font color="#0D1B2A" size="10">{content}</font>'
    )
    return Paragraph(html, ParagraphStyle("sec", fontSize=10, leading=16, textColor=BLACK))
