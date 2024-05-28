// Sample hierarchical data
const data = {
  name: "root",
  children: [
      {
          name: "child1",
          children: [
              { name: "child1-1" },
              { name: "child1-2" }
          ]
      },
      { name: "child2" }
  ]
};

// Function to calculate chart height
function calculateChartHeight(root, barStep, marginTop, marginBottom) {
  let max = 1;
  root.each(d => {
      if (d.children) {
          max = Math.max(max, d.children.length);
      }
  });
  return max * barStep + marginTop + marginBottom;
}

// Function to create the chart
function createChart(root, width, height, barStep) {
  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, height])
      .attr("width", width)
      .attr("height", height)
      .attr("style", "max-width: 100%; height: auto;");

  const g = svg.append("g")
      .attr("transform", `translate(20,20)`);

  const node = g.selectAll(".node")
      .data(root.descendants())
      .enter().append("g")
      .attr("class", "node")
      .attr("transform", (d, i) => `translate(0,${i * barStep})`);

  node.append("rect")
      .attr("width", d => d.depth * 50 + 200)
      .attr("height", barStep - 1);

  node.append("text")
      .attr("dy", "0.35em")
      .attr("x", 5)
      .attr("y", barStep / 2)
      .text(d => d.data.name);

  return svg.node();
}

// Initialize chart
document.addEventListener('DOMContentLoaded', () => {
  const root = d3.hierarchy(data);
  const width = 800;
  const barStep = 30;
  const marginTop = 20;
  const marginBottom = 20;
  const height = calculateChartHeight(root, barStep, marginTop, marginBottom);

  const chart = createChart(root, width, height, barStep);
  document.getElementById('chart').appendChild(chart);
});
