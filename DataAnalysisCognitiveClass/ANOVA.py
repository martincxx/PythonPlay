"""ANOVA
it is used for finding correlation between different groups of a categorical variable

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html
"""
import scipy.stats as stats

df_anova = df[["make", "price"]]

grouped_anova= df_anova.groupby([["make"]])

anova_results_l=stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("subaru")["price"])

anova_results_l=stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("jaguar")["price"])
