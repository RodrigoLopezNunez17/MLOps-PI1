import matplotlib.pyplot as plt, seaborn as sns, pandas as pd

class Tools:
    def __init__(self) -> None:
        pass

    def PlotCategoricalFrequency(data:pd.Series, title:str, color1:str, color2:str, subtitle1:str, ytitle1:str, xlabel1:str, subtitle2:str, ytitle2:str, xlabel2:str)->plt.plot:
        d = data.value_counts()

        fig, (ax1, ax2) = plt.subplots(2,1)
        fig.set_figheight(7)
        fig.set_figwidth(15)
        fig.suptitle(title, fontsize=20)

        sns.barplot(x=d.index[:10], y=d[:10],ax=ax1, color=color1)
        ax1.set_title(subtitle1, fontsize=15)
        ax1.set_ylabel(ytitle1)
        ax1.set_xlabel(xlabel1)

        sns.barplot(x=d.index[-10:], y=d[-10:], ax=ax2, color=color2)
        ax2.set_title(subtitle2, fontsize=15)
        ax2.set_ylabel(ytitle2)

        plt.tight_layout()
        plt.show()