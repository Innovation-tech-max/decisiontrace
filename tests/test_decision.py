from app.models.decision import Decision

def test_decision_schema():
    decision = Decision(
        decision="Use RabbitMQ",
        alternatives=["Kafka"],
        rationale=["Current workload is around 2,000 events per second."],
        assumptions=["Traffic remains below 10,000 events per second."],
        review_triggers=["Traffic exceeds 10,000 events per second."],
    )

    assert decision.decision == "Use RabbitMQ"
    assert "Kafka" in decision.alternatives
    assert len(decision.rationale) > 0
    assert len(decision.assumptions) > 0
    assert len(decision.review_triggers) > 0