import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display


# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------

df = pd.read_pickle('MetaMotion/data_resampled.pkl')


# --------------------------------------------------------------
# Plot single columns
# --------------------------------------------------------------

set_df = df[df["set"] == 1]
plt.plot(set_df["acc_x"])

plt.plot(set_df["acc_y"].reset_index(drop = True))


# --------------------------------------------------------------
# Plot all exercises
# --------------------------------------------------------------


df["label"].unique() 


for label in df["label"].unique() :

    subset = df[df["label"] == label]
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=set_df["acc_y"].reset_index(drop=True), mode='lines', name=label))
    fig.update_layout(title='Accelerometer Readings',
                  xaxis_title='Sample Number',
                  yaxis_title='Acceleration (y-axis)')
    fig.show()

# --------------------------------------------------------------
# Adjust plot settings
# --------------------------------------------------------------

# --------------------------------------------------------------
# Compare medium vs. heavy sets
# --------------------------------------------------------------


category_df = df.query("label == 'squat' ").query("participant == 'A' ").reset_index()

category_df.groupby("category")['acc_y'].plot()


# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------

participant_df = df.query("label == 'bench' ").sort_values("participant").reset_index()

participant_df.groupby("participant")['acc_y'].plot()


# --------------------------------------------------------------
# Plot multiple axis
# --------------------------------------------------------------


label = "squat"
participant = "A"
all_axis_df = df.query(f" label == '{label}' ").query(f" participant == '{participant}' ").reset_index()


fig , ax = plt.subplots()
all_axis_df[["acc_x","acc_y","acc_z"]].plot(ax = ax)
ax.set_ylabel("acc_y")
ax.set_xlabel("samples")
plt.legend()


# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------


labels = df["label"].unique()
participants = df["participant"].unique()

for label in labels:
    for participant in participants:

        all_axis_df = df.query(f" label == '{label}' ").query(f" participant == '{participant}' ").reset_index()

        if len(all_axis_df) > 0:

            fig , ax = plt.subplots()
            all_axis_df[["acc_x","acc_y","acc_z"]].plot(ax = ax)
            ax.set_ylabel("acc_y")
            ax.set_xlabel("samples")
            plt.title(f"{label} ({participant})".title())
            plt.legend()

for label in labels:
    for participant in participants:

        all_axis_df = df.query(f" label == '{label}' ").query(f" participant == '{participant}' ").reset_index()

        if len(all_axis_df) > 0:

            fig , ax = plt.subplots()
            all_axis_df[["gyr_x","gyr_y","gyr_z"]].plot(ax = ax)
            ax.set_ylabel("acc_y")
            ax.set_xlabel("samples")
            plt.title(f"{label} ({participant})".title())
            plt.legend()


# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------


label = "row"
participant = "A"
combined_plot_df = df.query(f" label == '{label}' ").query(f" participant == '{participant}' ").reset_index(drop=True)


fig ,ax = plt.subplots(nrows=2, sharex=True,figsize=(20,10))
combined_plot_df[["acc_x","acc_y","acc_z"]].plot(ax = ax[0])
combined_plot_df[["gyr_x","gyr_y","gyr_z"]].plot(ax = ax[1])

ax[0].legend(loc="upper center", bbox_to_anchor=(0.5,0.5),ncol=3,fancybox=True,shadow=True)
ax[1].legend(loc="upper center", bbox_to_anchor=(0.5,0.5),ncol=3,fancybox=True,shadow=True)
ax[1].set_xlabel("samples")



# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------

labels = df["label"].unique()
participants = df["participant"].unique()

for label in labels:
    for participant in participants:

        combined_plot_df = df.query(f" label == '{label}' ").query(f" participant == '{participant}' ").reset_index()

        if len(combined_plot_df) > 0:

            fig ,ax = plt.subplots(nrows=2, sharex=True,figsize=(20,10))
            combined_plot_df[["acc_x","acc_y","acc_z"]].plot(ax = ax[0])
            combined_plot_df[["gyr_x","gyr_y","gyr_z"]].plot(ax = ax[1])

            ax[0].legend(loc="upper center", bbox_to_anchor=(0.5,0.5),ncol=3,fancybox=True,shadow=True)
            ax[1].legend(loc="upper center", bbox_to_anchor=(0.5,0.5),ncol=3,fancybox=True,shadow=True)
            ax[1].set_xlabel("samples")
            

            plt.savefig(f"figures/{label.title()} ({participant}).png")
            plt.show()








