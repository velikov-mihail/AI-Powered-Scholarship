# AI--Powered--Scholarship
Code used in [Novy-Marx and Velikov (2024b), AI-Powered (Finance) Scholarship.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5060022)

We first mine 30K+ potential stock return predictor signals from accounting data, and apply
the Novy-Marx and Velikov (2024) “Assaying Anomalies” protocol to generate
standardized “template reports” for 96 signals that pass the protocol’s rigorous
criteria. Each report details a signal’s performance predicting stock returns
using a wide array of tests and benchmarks it to more than 200 other known
anomalies. Finally, we use state-of-the-art LLMs to generate three distinct
complete versions of academic papers for each signal. You can find a description of the signals and links to the generated papers in the following table:

<table border='1' style='border-collapse: collapse; text-align: center;'>
<tr>
<th>Numerator</th><th>Denominator</th><th>Signal Type</th><th>LLM-generated Signal Name</th>
<th colspan='3'>Links to Paper Versions</th>
</tr>
<tr>
<td>ACT</td><td>EBITDA</td><td>ratio</td><td>Operating Liquidity Margin</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACTEBITDA_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACTEBITDA_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACTEBITDA_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>AM</td><td>EBITDA</td><td>ratio</td><td>Intangibles-to-EBITDA</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AMEBITDA_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AMEBITDA_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AMEBITDA_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>AOLOCH</td><td>DPACT</td><td>ratio</td><td>Net Asset Impact to Depreciation</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHDPACT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHDPACT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHDPACT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>AOLOCH</td><td>XINT</td><td>ratio</td><td>Growth Impact Efficiency Metric</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHXINT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHXINT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHXINT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CH</td><td>EBITDA</td><td>ratio</td><td>Profitable Liquidity Score</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBITDA_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBITDA_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBITDA_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CH</td><td>EBIT</td><td>ratio</td><td>Cash Earnings Proportion</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBIT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBIT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBIT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CH</td><td>OIADP</td><td>ratio</td><td>Cash Profitability Index</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHOIADP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHOIADP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHOIADP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CAPS</td><td>XSGA</td><td>ratio</td><td>Efficiency of Expense Allocation</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCAPSXSGA_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCAPSXSGA_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCAPSXSGA_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>ACT</td><td>NOPIO</td><td>diff</td><td>Asset Income Spread</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDACTNOPIO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDACTNOPIO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDACTNOPIO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>AQC</td><td>ACT</td><td>diff</td><td>Acquisitions Efficiency Ratio</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCACT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCACT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCACT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>AQC</td><td>RECCO</td><td>diff</td><td>Acquisition Adjusted Receivables Current</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCRECCO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCRECCO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCRECCO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>AT</td><td>NOPIO</td><td>diff</td><td>Asset Nonop Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDATNOPIO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDATNOPIO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDATNOPIO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CEQ</td><td>CHE</td><td>diff</td><td>Equity to Cash Scale</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQCHE_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQCHE_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQCHE_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CEQL</td><td>CHE</td><td>diff</td><td>Cash Liquidity Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQLCHE_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQLCHE_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQLCHE_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CEQ</td><td>NOPIO</td><td>diff</td><td>Equity Scale Diff</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQNOPIO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQNOPIO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQNOPIO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>ACOX</td><td>diff</td><td>Asset Efficiency Margin</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACOX_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACOX_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACOX_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>ACT</td><td>diff</td><td>Stock Asset Delta</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>AOX</td><td>diff</td><td>Stock-to-Asset Spread</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAOX_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAOX_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAOX_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>AO</td><td>diff</td><td>Equity Dilution Factor</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>AT</td><td>diff</td><td>Equity Efficiency</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>CAPS</td><td>diff</td><td>Equity Adjustment Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPS_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPS_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPS_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>CAPXV</td><td>diff</td><td>Capital Stock Utilization Delta</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPXV_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPXV_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPXV_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>CAPX</td><td>diff</td><td>Stock Investment Efficiency Signal</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPX_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPX_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPX_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>CEQL</td><td>diff</td><td>Net Ownership Stake</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQL_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQL_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQL_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>CEQ</td><td>diff</td><td>Equity Share Deviation</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQ_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQ_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQ_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>CHE</td><td>diff</td><td>Stock Cash Differential</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCHE_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCHE_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCHE_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>COGS</td><td>diff</td><td>Inventory Efficiency Ratio</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCOGS_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCOGS_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCOGS_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>CSTK</td><td>diff</td><td>Stock Ownership Contrast</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCSTK_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCSTK_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCSTK_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>DLC</td><td>diff</td><td>Equity Weighted Debt Scale</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLC_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLC_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLC_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>DLTT</td><td>diff</td><td>Equity Debt Differential</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLTT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLTT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLTT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>DPACT</td><td>diff</td><td>Stock Depreciation Difference Signal</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDPACT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDPACT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDPACT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>DP</td><td>diff</td><td>Stock Depreciation Gradient</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>DVC</td><td>diff</td><td>Stock Dividend Relationship Index</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVC_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVC_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVC_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>DVT</td><td>diff</td><td>Stock Dividend Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>EMP</td><td>diff</td><td>Employees per Share Sensitivity</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKEMP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKEMP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKEMP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>GP</td><td>diff</td><td>Stock-Gross Profit Contrast</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKGP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKGP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKGP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>ICAPT</td><td>diff</td><td>Shareholder Capital Efficiency Difference</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKICAPT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKICAPT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKICAPT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>INTAN</td><td>diff</td><td>Stock-Intangible Disparity</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKINTAN_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKINTAN_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKINTAN_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>INVT</td><td>diff</td><td>Stock Inventory Delta</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKINVT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKINVT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKINVT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>LCT</td><td>diff</td><td>Stock Liability Differential Signal</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLCT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLCT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLCT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>LT</td><td>diff</td><td>Equity Liability Differential</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>PPEGT</td><td>diff</td><td>Stock-PPE Scale Signal</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPEGT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPEGT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPEGT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>PPENT</td><td>diff</td><td>Net Asset Utilization Gap</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPENT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPENT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPENT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>RECCO</td><td>diff</td><td>Stock and Receivables Relationship</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKRECCO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKRECCO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKRECCO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>RECT</td><td>diff</td><td>Inventory Adjusted Cash Flow</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKRECT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKRECT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKRECT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>SALE</td><td>diff</td><td>Stock Sales Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSALE_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSALE_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSALE_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>SEQ</td><td>diff</td><td>Stock Equity Imbalance Scale</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSEQ_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSEQ_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSEQ_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>TXDITC</td><td>diff</td><td>Tax-Adjusted Stock Difference</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKTXDITC_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKTXDITC_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKTXDITC_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>XINT</td><td>diff</td><td>Stock-Impact Ratio</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXINT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXINT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXINT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>XOPR</td><td>diff</td><td>Operating Expense Normalized Common Stock Difference</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXOPR_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXOPR_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXOPR_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>XRENT</td><td>diff</td><td>Stock-Rental Discrepancy Signal</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXRENT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXRENT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXRENT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>CSTK</td><td>XSGA</td><td>diff</td><td>Revenue Efficiency Factor</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXSGA_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXSGA_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXSGA_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>ACT</td><td>diff</td><td>Debt Asset Differential</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISACT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISACT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISACT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>AOX</td><td>diff</td><td>Debt Issuance Impact Factor</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAOX_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAOX_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAOX_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>AT</td><td>diff</td><td>Debt Issuance Efficiency</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>CAPS</td><td>diff</td><td>Debt Surplus Delta</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPS_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPS_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPS_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>CAPXV</td><td>diff</td><td>Capital Expenditure to Long-term Debt Issuance Differential</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPXV_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPXV_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPXV_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>CAPX</td><td>diff</td><td>Debt Funding Efficiency</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPX_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPX_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPX_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>CEQL</td><td>diff</td><td>Debt-Equity Liquidity Gap</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQL_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQL_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQL_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>CEQ</td><td>diff</td><td>Equity-Debt Imbalance Factor</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQ_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQ_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQ_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>DPACT</td><td>diff</td><td>Capital Debt Depreciation Delta</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDPACT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDPACT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDPACT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>DP</td><td>diff</td><td>Debt Depreciation Scale</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>EBITDA</td><td>diff</td><td>Debt Capacity Shift</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBITDA_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBITDA_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBITDA_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>EBIT</td><td>diff</td><td>Debt Issue Impact on EBIT</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBIT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBIT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBIT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>GP</td><td>diff</td><td>Debt-Issuance Gross Profit Delta</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISGP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISGP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISGP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>ICAPT</td><td>diff</td><td>Debt Capital Gap</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISICAPT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISICAPT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISICAPT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>OIADP</td><td>diff</td><td>Debt Impact Efficiency Score</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISOIADP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISOIADP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISOIADP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>PPEGT</td><td>diff</td><td>Capital Funding Efficiency Margin</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPEGT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPEGT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPEGT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>PPENT</td><td>diff</td><td>Debt-Issuance-PPE Scale Offset</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPENT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPENT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPENT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>RECCO</td><td>diff</td><td>Debt Impact Factor</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISRECCO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISRECCO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISRECCO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>SALE</td><td>diff</td><td>Debt Impact on Sales Growth</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSALE_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSALE_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSALE_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>SEQ</td><td>diff</td><td>Equity Impact Divergence</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSEQ_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSEQ_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSEQ_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>XOPR</td><td>diff</td><td>Debt-Efficiency Score</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXOPR_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXOPR_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXOPR_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>DLTIS</td><td>XRENT</td><td>diff</td><td>Rent-scaled Debt Emission Deviation</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXRENT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXRENT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXRENT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>FATE</td><td>NOPI</td><td>diff</td><td>Property Machinery Nonop Income Discrepancy</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFATENOPI_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFATENOPI_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFATENOPI_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>FINCF</td><td>PPEGT</td><td>diff</td><td>Asset Financing Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFPPEGT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFPPEGT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFPPEGT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>ICAPT</td><td>NI</td><td>diff</td><td>Profitable Investment Flow</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNI_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNI_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNI_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>ICAPT</td><td>NOPIO</td><td>diff</td><td>Capital Scale Nonop Diff</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNOPIO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNOPIO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNOPIO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>INVT</td><td>NP</td><td>diff</td><td>Inventory Payment Pressure Margin</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTNP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTNP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTNP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>INVT</td><td>XSGA</td><td>diff</td><td>Inventory Efficiency Operating Factor</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTXSGA_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTXSGA_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTXSGA_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>LCT</td><td>NOPIO</td><td>diff</td><td>Nonop Liability Contrast</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDLCTNOPIO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDLCTNOPIO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDLCTNOPIO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>NP</td><td>CEQT</td><td>diff</td><td>Equity-Debt Slant</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDNPCEQT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDNPCEQT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDNPCEQT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>PPENT</td><td>NOPIO</td><td>diff</td><td>Asset Utilization Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPIO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPIO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPIO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>PPENT</td><td>NOPI</td><td>diff</td><td>Net Property Plant and Equipment to Nonoperating Income Scale</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPI_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPI_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPI_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>RECTR</td><td>NOPIO</td><td>diff</td><td>Receipts Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDRECTRNOPIO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDRECTRNOPIO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDRECTRNOPIO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>SEQ</td><td>NOPIO</td><td>diff</td><td>Equity Impact Scale</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDSEQNOPIO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDSEQNOPIO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDSEQNOPIO_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>ICAPT</td><td>XSGA</td><td>ratio</td><td>Operating Efficiency Margin</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGICAPTXSGA_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGICAPTXSGA_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGICAPTXSGA_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>TXDFED</td><td>EBIT</td><td>ratio</td><td>Tax Shield Sensitivity Factor</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDEBIT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDEBIT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDEBIT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>TXDFED</td><td>OIADP</td><td>ratio</td><td>Tax Deprec Profit Impact</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDOIADP_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDOIADP_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDOIADP_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>OANCF</td><td>CSTK</td><td>ratio</td><td>Cash Flow to Equity</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCSTK_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCSTK_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCSTK_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>OANCF</td><td>DLC</td><td>ratio</td><td>Cash Flow Sustainability Index</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDLC_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDLC_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDLC_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>TXC</td><td>DVC</td><td>ratio</td><td>Tax-Effectiveness Yield</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXCDVC_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXCDVC_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXCDVC_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>TXFED</td><td>DVC</td><td>ratio</td><td>Tax Dividend Efficiency Score</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVC_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVC_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVC_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>TXFED</td><td>DVT</td><td>ratio</td><td>Tax Dividend Coverage Metric</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVT_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVT_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVT_modified_v3.pdf'>v3</a></td>
</tr>
<tr>
<td>TXPD</td><td>AO</td><td>ratio</td><td>Tax Efficiency</td>
<td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXPDAO_modified_v1.pdf'>v1</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXPDAO_modified_v2.pdf'>v2</a></td><td><a href='https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXPDAO_modified_v3.pdf'>v3</a></td>
</tr>
</table>

This repository contains code used to generate the papers as described in Novy-Marx and Velikov (2024b), AI-Powered (Finance) Scholarship. This code is to be used in conjunction with the MATLAB asset pricing package that accompanies Novy-Marx and Velikov (2024a), Assaying Anomalies. 

The order of operations is:

## Setup Instructions

### 1. MATLAB Toolkit Installation
Before running any scripts, you must first:
1. Download and install the MATLAB Toolkit from [AssayingAnomalies](https://github.com/velikov-mihail/AssayingAnomalies.git)
2. Follow the setup instructions in the AssayingAnomalies repository
3. **Important**: The results in Novy-Marx and Velikov (2024b) use the pre-release v0.4 of the MATLAB Toolkit. Ensure you're using this version for consistency.

## Main Pipeline Scripts

### 1. generate_template_reports.m
This MATLAB script sets up the initial data processing pipeline and performs the following operations:

1. Sets up the MATLAB environment and establishes necessary paths
2. Downloads COMPUSTAT variables
3. Creates annual market equity data
4. Runs 30K+ univariate sorts
5. Stores results in `results.mat`
6. Filters results
7. Runs the Assaying Anomalies protocol on the filtered signals

### Prerequisites
- MATLAB installation
- Access to COMPUSTAT database
- Required MATLAB packages:
  - Asset Pricing Package (located in `/scratch/mjv5465/Assaying-Anomalies-main/`)
  - Paper-specific package (located in `/scratch/mjv5465/Assaying-Anomalies-main/Scratch/`)
  - AssayingAnomalies Toolkit v0.4

## 2. get_variable_names.py
This Python script processes the COMPUSTAT variables and generates meaningful names for financial signals:

1. Connects to OpenAI's API (requires API key)
2. Loads COMPUSTAT variable dictionary from `compustat_variable_dictionary.csv`
3. Processes signals from `signals.csv`
4. Uses GPT-3.5-turbo to generate descriptive names and acronyms for financial signals
5. Outputs results to `signals_df.csv`

### Prerequisites
- Python environment
- Required Python packages:
  - openai
  - pandas
- OpenAI API key
- Input files:
  - `compustat_variable_dictionary.csv`
  - `signals.csv`

## 3. main.py
This script generates research paper versions using the processed signals:

1. Loads processed signals from `signals_df.csv`
2. Processes LaTeX templates
3. Generates multiple versions of research papers for each signal
4. Stores output in the `./tex/` directory

### Prerequisites
- Python environment
- Required Python packages:
  - pandas
- Custom modules:
  - `models.py` (containing `Signal` and `LLMPaperGenerator` classes)
- Access to Anthropic's Claude API

## Configuration
- Base directory: `./tex/`
- Default number of signals: 5
- Default number of versions per signal: 3
- LLM Configuration:
  - Model: claude-3-5-sonnet-latest
  - Temperature: 0.2
  - Max tokens: 8192

## Output Files
- `signals_df.csv`: Processed signals with generated names and acronyms
- LaTeX files: Generated in `./tex/` directory with naming format `{signal.var_name}.tex`
- Multiple versions of research papers for each signal

## Important Notes
1. Ensure all prerequisites are installed before running the scripts
2. API keys should be properly configured
3. File paths in `generate_template_reports.m` may need to be adjusted based on your system setup
4. The OpenAI API key in the code should be replaced with your own key or stored securely
5. The scripts should be run sequentially in the order presented above
6. Make sure you're using v0.4 of the AssayingAnomalies Toolkit for consistent results

## Error Handling
- The scripts include basic error handling for file not found scenarios
- Check the console output for any error messages during execution

## References

Novy-Marx, Robert, and Mihail Velikov. 2024a. "Assaying Anomalies." Working Paper.

Novy-Marx, Robert, and Mihail Velikov. 2024b. "AI-Powered (Finance) Scholarship." Working Paper.

## Suggested Citation

To cite this work, please use:

```bibtex

@article{Novy-MarxVelikov2024,
    title={AI-Powered (Finance) Scholarship},
    author={Novy-Marx, Robert and Velikov, Mihail},
    journal={Working Paper},
    year={2024}
}
