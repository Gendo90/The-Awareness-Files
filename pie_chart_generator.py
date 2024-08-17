import pandas as pd

def generate_pie_chart(file_path):
    pie_chart_data = pd.read_excel(file_path, header=None)

    pie_chart_series = pie_chart_data.squeeze(axis=0)
    print(pie_chart_series)
    result = pie_chart_series.plot(
        kind="pie", autopct="%.2f", y=1, labels=pie_chart_series[0], legend=False, title="", ylabel="")
    fig = result.get_figure()
    fig.savefig('./pie_chart_output/{}.svg'.format(file_path.split("/")[-1]))

if __name__ == "__main__":
    # run function with input file
    print("please input the file path:")
    file_path = input().strip()

    generate_pie_chart(file_path)