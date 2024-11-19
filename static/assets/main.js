// Hàm tạo biểu đồ bằng Billboard.js
function createChart() {
  const array = JSON.parse(document.getElementById("arrayInput").value);
  console.log(array);
  bb.generate({
    bindto: "#chart",
    data: {
      columns: [["data", ...array]],
    },
  });
}

// Hàm xử lý việc gửi dữ liệu đến server và nhận kết quả
async function findMax() {
  const position = parseInt(document.getElementById("positionInput").value);
  const array = JSON.parse(document.getElementById("arrayInput").value);

  try {
    // Gửi dữ liệu đến API Flask
    const response = await fetch("/solve", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ array: array, position: position }),
    });

    if (response.ok) {
      const data = await response.json();
      document.getElementById(
        "result"
      ).innerText = `Maximum value: ${data.max_value}`;
      bb.generate({
        bindto: "#chart",
        data: {
          columns: [["data", ...array]],
          color: function (color, d) {
            return d.value === data.max_value ? "#FF0000" : "#4F81BD";
          },
        },
      });
    } else {
      const error = await response.json();
      document.getElementById("result").innerText = `Error: ${error.error}`;
    }
  } catch (err) {
    document.getElementById("result").innerText =
      "Error processing your request.";
  }
}
