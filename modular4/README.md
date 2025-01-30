<h1>PDM Chain and Product Rule Motor Analysis</h1>

<p>This repository contains a Python script that utilizes the <b>Chain Rule</b> and <b>Product Rule</b> to analyze engine efficiency based on various factors such as temperature, vibration, load, and wear rate.</p>

<h2>Use Case</h2>

<ul>
  <li><b>Chain Rule:</b> Used to compute the rate of change of engine efficiency over time, considering temperature and vibration effects.</li>
  <li><b>Product Rule:</b> Applied to compute how engine efficiency changes when multiple variables (like load and wear rate) interact.</li>
</ul>

<h2>Features</h2>

<ul>
  <li>Calculates <b>engine efficiency</b> based on:
    <ul>
      <li>Temperature</li>
      <li>Vibration</li>
      <li>Load</li>
    </ul>
  </li>
  <li>Computes <b>partial derivatives</b> using the Chain Rule:
    <ul>
      <li>With respect to Temperature</li>
      <li>With respect to Vibration</li>
    </ul>
  </li>
  <li>Uses the <b>Product Rule</b> to determine how load and wear rate interact over time.</li>
</ul>

<h2>Installation</h2>

<p>To run the script, ensure you have Python installed along with NumPy. You can install dependencies using:</p>

<pre>
<code>pip install numpy</code>
</pre>

<h2>Usage</h2>

<p>Run the script:</p>

<pre>
<code>python pdm_chain_prod_rule_motor.py</code>
</pre>

<p>The script prints a table with:</p>

<ul>
  <li>Time steps</li>
  <li>Engine Efficiency</li>
  <li>Partial derivatives (with respect to temperature & vibration)</li>
  <li>Product Rule results for load and wear rate</li>
</ul>

<h2>Example Output</h2>

<pre>
Time (hrs) | Efficiency | dEff/dTemp | dEff/dVib | Product Rule d(Load*Wear)/dt
--------------------------------------------------------------------------------
0.0        | 0.3679     | -0.0037    | -0.0184   | 1.0000
2.5        | 0.2907     | -0.0029    | -0.0145   | 0.9840
5.0        | 0.2225     | -0.0022    | -0.0111   | 0.9720
7.5        | 0.1955     | -0.0020    | -0.0098   | 0.9600
10.0       | 0.1624     | -0.0016    | -0.0081   | 0.9480
</pre>

<h2>License</h2>

<p>This project is licensed under the MIT License.</p>

<h2>Contributing</h2>

<p>Feel free to fork this repository and submit pull requests.</p>


