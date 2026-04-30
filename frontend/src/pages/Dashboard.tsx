import BalanceCard from "../component/BalCard";
import { useEffect } from "react";
import PayForm from "../component/PayForm";
import PayoutTable from "../component/PayTable";
import { usePay } from "../hooks/usePay";
import { useBalance } from "../hooks/useBalance";

export default function Dashboard() {
    const { payout, fetchPayouts } = usePay();
    const { balance, fetchBalance } = useBalance();

    useEffect(() => {
        const interval = setInterval(() => {
            fetchBalance();
            fetchPayouts();
        }, 3000);

        return () => clearInterval(interval);
    }, []);

    return (
        <div style={{ padding: 20 }}>
            <h1>Merchant Dashboard</h1>

            <BalanceCard balance={balance} />

            <PayForm
                onSuccess={() => {
                    fetchBalance();
                    fetchPayouts();
                }}
            />

            <h2>Payout History</h2>
            <PayoutTable payouts={payout} />
        </div>
    );
}