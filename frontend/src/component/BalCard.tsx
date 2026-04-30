interface Props {
    balance: number;
}

export default function BalCard({ balance }: Props) {
    return (
        <div style={{ padding: 20, border: "1px solid #ccc" }}>
            <h2>Balance</h2>
            <p>₹ {balance}</p>
        </div>
    );
}