export const generateDocs = async (prompt) => {
  const response = await fetch("http://localhost:8000/generate/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt })
  });
  return response.json();
};
