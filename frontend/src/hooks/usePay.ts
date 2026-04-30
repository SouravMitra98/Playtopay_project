import { useEffect, useState } from "react";

interface Payout {
    id: number;
    status: string;
    amount: number;
}

export function usePay() {
    const [payout, setPayout] = useState<Payout[]>([]);

    const fetchPayouts = async () => {
        try {
            const res = await fetch("http://127.0.0.1:8000/api/v1/payouts/");
            const data = await res.json();
            console.log("GET DATA:", data);
            setPayout(data);
        } catch (err) {
            console.error("Failed to fetch payouts:", err);
        }
    };

    useEffect(() => {
        let mounted = true;

        const run = async () => {
            if (mounted) {
                await fetchPayouts();
            }
        };

        run(); // initial load

        const interval = setInterval(() => {
            if (mounted) {
                fetchPayouts();
            }
        }, 2000);

        return () => {
            mounted = false;
            clearInterval(interval);
        };
    }, []);

    return { payout, fetchPayouts };
}