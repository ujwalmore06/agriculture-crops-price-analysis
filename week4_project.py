import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =========================================================
# 1. LOAD DATA
# =========================================================

file_path = "/Users/ujwalmore/Downloads/agricultural_market_prices.csv"

df = pd.read_csv(
    file_path,
    header=None,
    names=[
        "Date",
        "State",
        "District",
        "Market",
        "Crop",
        "Variety",
        "Min_Price",
        "Max_Price",
        "Modal_Price"
    ]
)

# =========================================================
# 2. DATA CLEANING
# =========================================================

df = df.drop_duplicates()

df["Min_Price"] = pd.to_numeric(
    df["Min_Price"], errors="coerce"
)

df["Max_Price"] = pd.to_numeric(
    df["Max_Price"], errors="coerce"
)

df["Modal_Price"] = pd.to_numeric(
    df["Modal_Price"], errors="coerce"
)

df["Min_Price"] = df["Min_Price"].fillna(
    df["Min_Price"].mean()
)

df["Max_Price"] = df["Max_Price"].fillna(
    df["Max_Price"].mean()
)

df["Modal_Price"] = df["Modal_Price"].fillna(
    df["Modal_Price"].mean()
)


# =========================================================
# 3. NUMPY
# =========================================================

prices = np.array(df["Modal_Price"])

average_price = np.mean(prices)
highest_price = np.max(prices)
lowest_price = np.min(prices)
standard_deviation = np.std(prices)

price_data = np.array([
    df["Min_Price"].values,
    df["Max_Price"].values,
    df["Modal_Price"].values
])


# =========================================================
# 4. MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("Agricultural Market Price Analysis")

root.geometry("1350x850")

root.configure(bg="#F4F8F4")


# =========================================================
# 5. COLORS
# =========================================================

DARK_GREEN = "#1B5E20"
GREEN = "#2E7D32"
LIGHT_GREEN = "#E8F5E9"

BLUE = "#1565C0"
LIGHT_BLUE = "#E3F2FD"

ORANGE = "#EF6C00"
LIGHT_ORANGE = "#FFF3E0"

PURPLE = "#6A1B9A"
LIGHT_PURPLE = "#F3E5F5"

RED = "#C62828"
LIGHT_RED = "#FFEBEE"

WHITE = "#FFFFFF"
DARK = "#263238"


# =========================================================
# 6. HEADER
# =========================================================

header = tk.Frame(
    root,
    bg=DARK_GREEN,
    height=90
)

header.pack(
    fill="x"
)

title = tk.Label(
    header,
    text="🌾 AGRICULTURAL MARKET PRICE ANALYSIS",
    font=("Arial", 25, "bold"),
    bg=DARK_GREEN,
    fg=WHITE
)

title.pack(pady=(15, 2))


subtitle = tk.Label(
    header,
    text="Smart analysis of agricultural crop market prices",
    font=("Arial", 12),
    bg=DARK_GREEN,
    fg="#C8E6C9"
)

subtitle.pack()


# =========================================================
# 7. SUMMARY CARDS
# =========================================================

summary_frame = tk.Frame(
    root,
    bg="#F4F8F4"
)

summary_frame.pack(
    pady=18
)


def create_card(
    parent,
    title_text,
    value_text,
    bg_color
):

    card = tk.Frame(
        parent,
        bg=bg_color,
        width=240,
        height=110
    )

    card.pack_propagate(False)

    title_label = tk.Label(
        card,
        text=title_text,
        font=("Arial", 11, "bold"),
        bg=bg_color,
        fg=DARK
    )

    title_label.pack(
        pady=(15, 5)
    )

    value_label = tk.Label(
        card,
        text=value_text,
        font=("Arial", 20, "bold"),
        bg=bg_color,
        fg=DARK
    )

    value_label.pack()

    return card


card1 = create_card(
    summary_frame,
    "📋 TOTAL RECORDS",
    str(len(df)),
    LIGHT_GREEN
)

card1.grid(
    row=0,
    column=0,
    padx=8
)


card2 = create_card(
    summary_frame,
    "💰 AVERAGE PRICE",
    "₹" + str(round(average_price, 2)),
    LIGHT_BLUE
)

card2.grid(
    row=0,
    column=1,
    padx=8
)


card3 = create_card(
    summary_frame,
    "📈 HIGHEST PRICE",
    "₹" + str(round(highest_price, 2)),
    LIGHT_ORANGE
)

card3.grid(
    row=0,
    column=2,
    padx=8
)


card4 = create_card(
    summary_frame,
    "📉 LOWEST PRICE",
    "₹" + str(round(lowest_price, 2)),
    LIGHT_RED
)

card4.grid(
    row=0,
    column=3,
    padx=8
)


# =========================================================
# 8. FILTER FRAME
# =========================================================

filter_frame = tk.Frame(
    root,
    bg=WHITE,
    bd=1,
    relief="solid"
)

filter_frame.pack(
    fill="x",
    padx=35,
    pady=8
)


filter_title = tk.Label(
    filter_frame,
    text="🔍 FILTER DATA",
    font=("Arial", 13, "bold"),
    bg=WHITE,
    fg=DARK_GREEN
)

filter_title.grid(
    row=0,
    column=0,
    padx=15,
    pady=12
)


# Crop dropdown

crop_label = tk.Label(
    filter_frame,
    text="Crop:",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg=DARK
)

crop_label.grid(
    row=0,
    column=1,
    padx=5
)


crop_var = tk.StringVar()

crop_combo = ttk.Combobox(
    filter_frame,
    textvariable=crop_var,
    values=["All Crops"] + sorted(
        df["Crop"].unique().tolist()
    ),
    state="readonly",
    width=18
)

crop_combo.current(0)

crop_combo.grid(
    row=0,
    column=2,
    padx=5
)


# District dropdown

district_label = tk.Label(
    filter_frame,
    text="District:",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg=DARK
)

district_label.grid(
    row=0,
    column=3,
    padx=5
)


district_var = tk.StringVar()

district_combo = ttk.Combobox(
    filter_frame,
    textvariable=district_var,
    values=["All Districts"] + sorted(
        df["District"].unique().tolist()
    ),
    state="readonly",
    width=18
)

district_combo.current(0)

district_combo.grid(
    row=0,
    column=4,
    padx=5
)


# =========================================================
# 9. FILTER FUNCTION
# =========================================================

def apply_filter():

    filtered_df = df.copy()

    selected_crop = crop_var.get()

    selected_district = district_var.get()

    if selected_crop != "All Crops":

        filtered_df = filtered_df[
            filtered_df["Crop"] == selected_crop
        ]

    if selected_district != "All Districts":

        filtered_df = filtered_df[
            filtered_df["District"] == selected_district
        ]

    if len(filtered_df) == 0:

        messagebox.showinfo(
            "No Data",
            "No records found."
        )

        return

    show_table(
        filtered_df
    )


# =========================================================
# 10. RESET FILTER
# =========================================================

def reset_filter():

    crop_combo.current(0)

    district_combo.current(0)

    show_table(df)


# =========================================================
# 11. FILTER BUTTON
# =========================================================

filter_button = tk.Button(
    filter_frame,
    text="Apply Filter",
    command=apply_filter,
    bg=GREEN,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    width=14
)

filter_button.grid(
    row=0,
    column=5,
    padx=10
)


reset_button = tk.Button(
    filter_frame,
    text="Reset",
    command=reset_filter,
    bg=ORANGE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    width=12
)

reset_button.grid(
    row=0,
    column=6,
    padx=5
)


# =========================================================
# 12. CHART FUNCTIONS
# =========================================================

def show_chart(title_text, chart_type):

    selected_crop = crop_var.get()

    selected_district = district_var.get()

    chart_df = df.copy()

    if selected_crop != "All Crops":

        chart_df = chart_df[
            chart_df["Crop"] == selected_crop
        ]

    if selected_district != "All Districts":

        chart_df = chart_df[
            chart_df["District"] == selected_district
        ]

    if len(chart_df) == 0:

        messagebox.showinfo(
            "No Data",
            "No data available for selected filter."
        )

        return

    window = tk.Toplevel(root)

    window.title(title_text)

    window.geometry("850x650")

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )


    # BAR

    if chart_type == "bar":

        data = chart_df.groupby(
            "Crop"
        )["Modal_Price"].mean()

        ax.bar(
            data.index,
            data.values
        )

        ax.set_xlabel(
            "Crop"
        )

        ax.set_ylabel(
            "Average Modal Price"
        )

        ax.set_title(
            "Crop-wise Average Market Price"
        )

        plt.xticks(
            rotation=45
        )


    # LINE

    elif chart_type == "line":

        ax.plot(
            chart_df["Date"],
            chart_df["Modal_Price"],
            marker="o"
        )

        ax.set_xlabel(
            "Date"
        )

        ax.set_ylabel(
            "Modal Price"
        )

        ax.set_title(
            "Agricultural Market Price Trend"
        )

        plt.xticks(
            rotation=45
        )


    # PIE

    elif chart_type == "pie":

        data = chart_df[
            "Crop"
        ].value_counts()

        ax.pie(
            data.values,
            labels=data.index,
            autopct="%1.1f%%"
        )

        ax.set_title(
            "Crop Distribution"
        )


    # HISTOGRAM

    elif chart_type == "histogram":

        ax.hist(
            chart_df["Modal_Price"],
            bins=5
        )

        ax.set_xlabel(
            "Modal Price"
        )

        ax.set_ylabel(
            "Frequency"
        )

        ax.set_title(
            "Modal Price Distribution"
        )


    # SCATTER

    elif chart_type == "scatter":

        ax.scatter(
            chart_df["Min_Price"],
            chart_df["Max_Price"]
        )

        ax.set_xlabel(
            "Minimum Price"
        )

        ax.set_ylabel(
            "Maximum Price"
        )

        ax.set_title(
            "Minimum Price vs Maximum Price"
        )


    plt.tight_layout()


    canvas = FigureCanvasTkAgg(
        fig,
        master=window
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill=tk.BOTH,
        expand=True
    )


# =========================================================
# 13. CHART BUTTONS
# =========================================================

chart_frame = tk.Frame(
    root,
    bg="#F4F8F4"
)

chart_frame.pack(
    pady=10
)


def chart_button(
    text,
    chart_type,
    color
):

    return tk.Button(
        chart_frame,
        text=text,
        command=lambda: show_chart(
            text,
            chart_type
        ),
        bg=color,
        fg=WHITE,
        font=("Arial", 10, "bold"),
        width=16,
        height=2,
        relief="flat"
    )


chart_button(
    "📊 Bar Chart",
    "bar",
    GREEN
).grid(
    row=0,
    column=0,
    padx=5
)


chart_button(
    "📈 Line Chart",
    "line",
    BLUE
).grid(
    row=0,
    column=1,
    padx=5
)


chart_button(
    "🥧 Pie Chart",
    "pie",
    PURPLE
).grid(
    row=0,
    column=2,
    padx=5
)


chart_button(
    "📉 Histogram",
    "histogram",
    ORANGE
).grid(
    row=0,
    column=3,
    padx=5
)


chart_button(
    "🔵 Scatter Plot",
    "scatter",
    RED
).grid(
    row=0,
    column=4,
    padx=5
)


# =========================================================
# 14. INSIGHTS
# =========================================================

def show_insights():

    crop_price = df.groupby(
        "Crop"
    )["Modal_Price"].mean()

    highest_crop = crop_price.idxmax()

    lowest_crop = crop_price.idxmin()

    messagebox.showinfo(
        "Market Insights",
        f"🌾 Highest Average Price Crop:\n"
        f"{highest_crop}\n\n"
        f"📉 Lowest Average Price Crop:\n"
        f"{lowest_crop}\n\n"
        f"💰 Overall Average Price:\n"
        f"₹{average_price:.2f}\n\n"
        f"📊 Standard Deviation:\n"
        f"{standard_deviation:.2f}"
    )


insight_button = tk.Button(
    root,
    text="💡 Show Market Insights",
    command=show_insights,
    bg=PURPLE,
    fg=WHITE,
    font=("Arial", 11, "bold"),
    width=25,
    height=2
)

insight_button.pack(
    pady=5
)


# =========================================================
# 15. DATA TABLE
# =========================================================

table_title = tk.Label(
    root,
    text="📋 MARKET PRICE DATA",
    font=("Arial", 14, "bold"),
    bg="#F4F8F4",
    fg=DARK_GREEN
)

table_title.pack(
    pady=(5, 3)
)


table_frame = tk.Frame(
    root,
    bg=WHITE
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=5
)


columns = list(df.columns)


tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)


for column in columns:

    tree.heading(
        column,
        text=column
    )

    tree.column(
        column,
        width=120,
        anchor="center"
    )


tree.pack(
    side="left",
    fill="both",
    expand=True
)


scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

scrollbar.pack(
    side="right",
    fill="y"
)

tree.configure(
    yscrollcommand=scrollbar.set
)


# =========================================================
# 16. SHOW TABLE FUNCTION
# =========================================================

def show_table(data):

    for item in tree.get_children():

        tree.delete(item)

    for _, row in data.iterrows():

        tree.insert(
            "",
            "end",
            values=list(row)
        )


show_table(df)


# =========================================================
# 17. EXPORT DATA
# =========================================================

def export_data():

    file_name = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[
            ("CSV Files", "*.csv")
        ]
    )

    if file_name:

        df.to_csv(
            file_name,
            index=False
        )

        messagebox.showinfo(
            "Success",
            "Data exported successfully!"
        )


export_button = tk.Button(
    root,
    text="📤 Export Data",
    command=export_data,
    bg=BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    width=18
)

export_button.pack(
    pady=8
)


# =========================================================
# 18. EXIT
# =========================================================

exit_button = tk.Button(
    root,
    text="EXIT",
    command=root.destroy,
    bg=RED,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    width=12
)

exit_button.pack(
    pady=(0, 12)
)


# =========================================================
# 19. START DASHBOARD
# =========================================================

root.mainloop()