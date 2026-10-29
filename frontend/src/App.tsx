import { useEffect, useState } from "react";

type ApiStatus = {
  status: string;
  message: string;
};

function App() {
  const [api, setApi] = useState<ApiStatus | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/health/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("API request failed");
        }
        return response.json();
      })
      .then(setApi)
      .catch(() => setError("Cannot connect to the backend"));
  }, []);

  return (
    <main className="min-h-screen bg-[#101010] p-8 text-white">
      <p className="text-sm uppercase tracking-[0.3em] text-red-500">
        F1 Herum
      </p>

      <h1 className="mt-6 text-4xl font-bold">Race data. Deeper analysis.</h1>

      <p className="mt-4 text-neutral-400">Explore Formula 1 through data.</p>

      <section className="mt-8 rounded-xl border border-neutral-800 p-5">
        <h2 className="font-semibold">Backend connection</h2>

        {api && <p className="mt-2 text-green-400">{api.message}</p>}
        {error && <p className="mt-2 text-red-400">{error}</p>}
        {!api && !error && <p className="mt-2">Connecting...</p>}
      </section>
    </main>
  );
}

export default App;
