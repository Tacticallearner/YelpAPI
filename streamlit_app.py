async function fetchYachtDetails() {
    try {
        const response = await fetch('https://api.yourapp.com/yachts', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                // Include API key if required
                // 'Authorization': 'Bearer YOUR_API_KEY'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();return (
    <div>
        {yachtData.length > 0 ? (
            yachtData.map((yacht, index) => (
                <div key={index}>
                    <h2>{yacht.name}</h2>
                    <p>Model: {yacht.yacht_details.model}</p>
                    // Other yacht details
                </div>
            ))
        ) : (
            <p>No yacht data available.</p>
        )}
    </div>
);

        return data;
    } catch (error) {
        console.error('Error fetching yacht details:', error);
    }
}
const [yachtData, setYachtData] = useState([]);

useEffect(() => {
    fetchYachtDetails().then(data => {
        if (data) {
            setYachtData(data);
        }
    });
}, []);
